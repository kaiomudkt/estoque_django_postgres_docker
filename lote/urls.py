from django.urls import path
from .views import atualiza_lote, deletar_lote, lista_lotes, cadastra_lote

urlpatterns = [
    path('', lista_lotes, name='lotes'),
    path('cadastrar', cadastra_lote, name='cadastra_lote'),
    path('atualizar<int:id>/', atualiza_lote, name='atualiza_lote'),
    path('deletar<int:id>/', deletar_lote, name='deletar_lote'),
]