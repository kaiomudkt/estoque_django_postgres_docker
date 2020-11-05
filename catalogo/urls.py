from django.urls import path

from .views import deletar_produto, CatalogoListar, CatalogoCadastrar, CatalogoAtualizar

urlpatterns = [
    path('', CatalogoListar.as_view(), name='catalogo'),
    path('cadastrar', CatalogoCadastrar.as_view(), name='cadastra_produto'),
    path('atualizar<int:id>/', CatalogoAtualizar.as_view(), name='atualiza_produto'),
    path('deletar<int:id>/', deletar_produto, name='deletar_produto'),
]
