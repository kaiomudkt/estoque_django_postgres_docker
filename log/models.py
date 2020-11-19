# from django.contrib.auth.models import User
from django.db import models

class LogCatalogo(models.Model):
    id_tabela = models.CharField(max_length=50, null=True)
    id_tupla = models.CharField(max_length=50, null=True)
    metodo = models.CharField(max_length=50, null=True)
    data = models.DateTimeField(auto_now_add=True)
    a_nome = models.CharField(max_length=255)
    n_nome = models.CharField(max_length=255)
    a_descricao = models.TextField()
    n_descricao = models.TextField()
    a_id_preco = models.CharField(max_length=50, null=True)
    n_id_preco = models.CharField(max_length=50, null=True)

class LogPreco(models.Model):
    id_tupla = models.CharField(max_length=50, null=True)
    metodo = models.CharField(max_length=50, null=True)
    data = models.DateTimeField(auto_now_add=True)
    a_dolar = models.DecimalField(max_digits=9, decimal_places=2)
    n_dolar = models.DecimalField(max_digits=9, decimal_places=2)
    a_real = models.DecimalField(max_digits=9, decimal_places=2)
    n_real = models.DecimalField(max_digits=9, decimal_places=2)

class LogFornecedor(models.Model):
    id_tupla = models.CharField(max_length=50, null=True)
    metodo = models.CharField(max_length=50, null=True)
    data = models.DateTimeField(auto_now_add=True)
    a_nome = models.CharField(max_length=255)
    n_nome = models.CharField(max_length=255)
    a_cnpj = models.CharField(max_length=255)
    n_cnpj = models.CharField(max_length=255)
    a_id_catalogo = models.CharField(max_length=50, null=True)
    n_id_catalogo = models.CharField(max_length=50, null=True)

class LogLote(models.Model):
    id_tupla = models.CharField(max_length=50, null=True)
    metodo = models.CharField(max_length=50, null=True)
    data = models.DateTimeField(auto_now_add=True)
    a_data_lote = models.DateTimeField(auto_now_add=True)
    n_data_lote = models.DateTimeField(auto_now_add=True)
    a_quantidade = models.IntegerField()
    n_quantidade = models.IntegerField()
    a_id_produtoFornecedor = models.CharField(max_length=50, null=True)
    n_id_produtoFornecedor = models.CharField(max_length=50, null=True)

class LogProdutoFornecedor(models.Model):
    id_tupla = models.CharField(max_length=50, null=True)
    metodo = models.CharField(max_length=50, null=True)
    data = models.DateTimeField(auto_now_add=True)
    a_id_fornecedor = models.CharField(max_length=50, null=True)
    n_id_fornecedor = models.CharField(max_length=50, null=True)
    a_id_produto = models.CharField(max_length=50, null=True)
    n_id_produto = models.CharField(max_length=50, null=True)
