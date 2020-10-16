from rest_framework import generics

from emprestimos.models import Emprestimo, Pagamento
from emprestimos.serializers import EmprestimoSerializer
from emprestimos.serializers import PagamentoSerializer


class EmprestimoList(generics.ListCreateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    name = 'emprestimo-list'

    def get_queryset(self):
        user = self.request.user
        return Emprestimo.objects.filter(owner__username=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EmprestimoDetail(generics.ListCreateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    name = 'emprestimo-detail'


class PagamentoList(generics.ListCreateAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
    name = 'pagamento-list'

    def get_queryset(self):
        user = self.request.user
        return Pagamento.objects.filter(owner__username=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PagamentoDetail(generics.ListCreateAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
    name = 'pagamento-detail'
