# from django.contrib.auth.models import User
from django.db import models

class LogCatalogo(models.Model):
    id_tabela = models.CharField(max_length=50, null=True)
    id_tupla = models.CharField(max_length=50, null=True)
    metodo = models.CharField(max_length=50, null=True)
    data = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    id_preco = models.CharField(max_length=50, null=True)

class LogPreco(models.Model):
    id_tupla = models.CharField(max_length=50, null=True)
    metodo = models.CharField(max_length=50, null=True)
    data = models.DateTimeField(auto_now_add=True)
    dolar = models.DecimalField(max_digits=9, decimal_places=2)
    real = models.DecimalField(max_digits=9, decimal_places=2)

class LogFornecedor(models.Model):
    id_tupla = models.CharField(max_length=50, null=True)
    metodo = models.CharField(max_length=50, null=True)
    data = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255)
    id_catalogo = models.CharField(max_length=50, null=True)

class LogLote(models.Model):
    id_tupla = models.CharField(max_length=50, null=True)
    metodo = models.CharField(max_length=50, null=True)
    data = models.DateTimeField(auto_now_add=True)
    data_lote = models.DateTimeField(auto_now_add=True)
    quantidade = models.IntegerField()
    id_produtoFornecedor = models.CharField(max_length=50, null=True)

class LogProdutoFornecedor(models.Model):
    id_tupla = models.CharField(max_length=50, null=True)
    metodo = models.CharField(max_length=50, null=True)
    data = models.DateTimeField(auto_now_add=True)
    id_fornecedor = models.CharField(max_length=50, null=True)
    id_produto = models.CharField(max_length=50, null=True)