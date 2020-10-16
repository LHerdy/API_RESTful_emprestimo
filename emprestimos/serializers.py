from rest_framework import serializers

from emprestimos.models import Emprestimo
from emprestimos.models import Pagamento

from django.contrib.auth.models import User


class UserEmprestimoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pagamento
        fields = (
            'url',
            'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    emprestimos = UserEmprestimoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'url',
            'pk',
            'username',
            'emprestimos')


class EmprestimoSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.ReadOnlyField(source='owner.username')
    pagamentos = serializers.HyperlinkedRelatedField(many=True, view_name='pagamento-detail',
                                                     read_only=True, write_only=())

    class Meta:
        model = Emprestimo
        fields = ['url', 'pk', 'id_emprestimo',
                  'usuario',
                  'data_da_solicitacao',
                  'banco',
                  'cliente',
                  'valor_nominal',
                  'parcelas',
                  'taxa_de_juros',
                  'total_pago',
                  'saldo_devedor',
                  'endereco_de_ip',
                  'pagamentos'
                  ]


class UserPagamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pagamento
        fields = (
            'url',
            'name')


class PagamentoSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.ReadOnlyField(source='owner.username')
    emprestimo = serializers.PrimaryKeyRelatedField(queryset=Emprestimo.objects.all(), many=False)

    class Meta:
        model = Pagamento
        fields = ['url', 'pk', 'id_pagamento',
                  'usuario',
                  'data_do_pagamento',
                  'emprestimo',
                  'valor_pago',
                  ]
