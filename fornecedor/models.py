from django.db import models
from catalogo.models import Catalogo
from lote.models import Lote

class Fornecedor(models.Model):
    produto = models.ManyToManyField(Catalogo)
    lote = models.ForeignKey(Lote)
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255)
