from django.db import models

from catalogo.models import Catalogo, Fornecedor


class Lote(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    quantidade = models.IntegerField()
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name='fornecedores')
    catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE, related_name='catalogo')
