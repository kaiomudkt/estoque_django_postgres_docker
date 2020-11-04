from django.urls import path

from .views import atualiza_produto, deletar_produto, CatalogoListar , cadastra_produto

urlpatterns = [
    path('', CatalogoListar.as_view(), name='catalogo'),
    path('cadastrar', cadastra_produto, name='cadastra_produto'),
    path('atualizar<int:id>/', atualiza_produto, name='atualiza_produto'),
    path('deletar<int:id>/', deletar_produto, name='deletar_produto'),
]
