from django.db import models

from catalogo.models import Catalogo


# from lote.models import Lote


class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255)
    catalogo = models.ManyToManyField(Catalogo, through='ProdutoFornecedor', through_fields=('produto', 'fornecedor'), blank=True, null=True)

    # def __str__(self):
    #     return "%s" % (self.nome)


class ProdutoFornecedor(models.Model):
    produto = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Catalogo, on_delete=models.CASCADE)
