
import uuid
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Emprestimo(models.Model):
    owner = models.ForeignKey(
        'auth.User',
        related_name='emprestimos',
        on_delete=models.CASCADE)
    id_emprestimo = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    banco = models.TextField(max_length=150)
    cliente = models.TextField(max_length=100)
    data_da_solicitacao = models.DateTimeField(auto_now_add=True, blank=True)
    valor_nominal = models.DecimalField(max_digits=13, decimal_places=2, validators=[
        MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    parcelas = models.IntegerField()
    taxa_de_juros = models.DecimalField(max_digits=13, decimal_places=2, validators=[
        MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    endereco_de_ip = models.GenericIPAddressField()

    @property
    def total_pago(self):
        total_pago = 0
        for pagamento in self.pagamentos.all():
            total_pago += pagamento.valor_pago
        return total_pago

    @property
    def saldo_devedor(self, ):
        i = (1 + self.taxa_de_juros / 100)
        fv = (self.valor_nominal * i ** self.parcelas)
        total = fv - self.total_pago
        return total

    class Meta:
        ordering = ('-data_da_solicitacao',)

    def __str__(self):
        return str(self.id_emprestimo)


class Pagamento(models.Model):
    owner = models.ForeignKey(
        'auth.User',
        related_name='pagamentos',
        on_delete=models.CASCADE)
    id_pagamento = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    emprestimo = models.ForeignKey(Emprestimo,
                                   related_name='pagamentos',
                                   on_delete=models.CASCADE)
    data_do_pagamento = models.DateTimeField(auto_now_add=True, blank=True)
    valor_pago = models.DecimalField(max_digits=13, decimal_places=2, validators=[
        MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))

    class Meta:
        ordering = ('-data_do_pagamento',)

    def __str__(self):
        return str(self.id_pagamento)
