from django.db import models

from catalogo.models import Catalogo


# from lote.models import Lote


class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255)
    # lote = models.ForeignKey(Lote, on_delete=models.CASCADE, related_name='lotes')
    catalogo = models.ManyToManyField(Catalogo)

    # def __str__(self):
    #     return "%s" % (self.nome)
