from django.conf.urls import url

from emprestimos import views

urlpatterns = [

    url(r'^emprestimos/', views.EmprestimoList.as_view(), name=views.EmprestimoList.name),
    url(r'^emprestimos/(?P<pk>[0-9]+)', views.EmprestimoDetail.as_view(), name=views.EmprestimoDetail.name),
    url(r'^pagamentos/', views.PagamentoList.as_view(), name=views.PagamentoList.name),
    url(r'^pagamentos/(?P<pk>[0-9]+)', views.PagamentoDetail.as_view(), name=views.PagamentoDetail.name),
]
