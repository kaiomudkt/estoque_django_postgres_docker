from django.urls import path

from .views import atualiza_fornecedor, deletar_fornecedor, lista_fornecedores, cadastra_fornecedor

urlpatterns = [
    path('', lista_fornecedores, name='fornecedores'),
    path('cadastrar', cadastra_fornecedor, name='cadastra_fornecedor'),
    path('atualizar<int:id>/', atualiza_fornecedor, name='atualiza_fornecedor'),
    path('deletar<int:id>/', deletar_fornecedor, name='deletar_fornecedor'),
]
