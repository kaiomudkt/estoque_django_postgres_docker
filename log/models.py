# from django.contrib.auth.models import User
from django.db import models
# a de antigo, n de novo
class LogCatalogo(models.Model):
    a_id_tupla = models.CharField(max_length=50, null=True)
    n_id_tupla = models.CharField(max_length=50, null=True)
    metodo = models.CharField(max_length=50, null=True)
    data = models.DateTimeField(auto_now_add=True)
    a_nome = models.CharField(max_length=255, blank=True, null=True)
    n_nome = models.CharField(max_length=255, blank=True, null=True)
    a_descricao = models.TextField(blank=True, null=True)
    n_descricao = models.TextField(blank=True, null=True)
    a_preco_id = models.CharField(max_length=50, null=True)
    n_preco_id = models.CharField(max_length=50, null=True)

class LogPreco(models.Model):
    a_id_tupla = models.CharField(max_length=50, null=True)
    n_id_tupla = models.CharField(max_length=50, null=True)
    metodo = models.CharField(max_length=50, null=True)
    data = models.DateTimeField(auto_now_add=True)
    a_dolar = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    n_dolar = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    a_real = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    n_real = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

class LogFornecedor(models.Model):
    a_id_tupla = models.CharField(max_length=50, null=True)
    n_id_tupla = models.CharField(max_length=50, null=True)
    metodo = models.CharField(max_length=50, null=True)
    data = models.DateTimeField(auto_now_add=True)
    a_nome = models.CharField(max_length=255, blank=True, null=True)
    n_nome = models.CharField(max_length=255, blank=True, null=True)
    a_cnpj = models.CharField(max_length=255, blank=True, null=True)
    n_cnpj = models.CharField(max_length=255, blank=True, null=True)
    # a_id_catalogo = models.CharField(max_length=50, null=True)
    # n_id_catalogo = models.CharField(max_length=50, null=True)

class LogLote(models.Model):
    a_id_tupla = models.CharField(max_length=50, null=True)
    n_id_tupla = models.CharField(max_length=50, null=True)
    metodo = models.CharField(max_length=50, null=True)
    data = models.DateTimeField(auto_now_add=True)
    a_data_lote = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    n_data_lote = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    a_quantidade = models.IntegerField(blank=True, null=True)
    n_quantidade = models.IntegerField(blank=True, null=True)
    a_produto_fornecedor_id = models.CharField(max_length=50, null=True)
    n_produto_fornecedor_id = models.CharField(max_length=50, null=True)

class LogProdutoFornecedor(models.Model):
    a_id_tupla = models.CharField(max_length=50, null=True)
    n_id_tupla = models.CharField(max_length=50, null=True)
    metodo = models.CharField(max_length=50, null=True)
    data = models.DateTimeField(auto_now_add=True)
    a_fornecedor_id = models.CharField(max_length=50, null=True)
    n_fornecedor_id = models.CharField(max_length=50, null=True)
    a_produto_id = models.CharField(max_length=50, null=True)
    n_produto_id = models.CharField(max_length=50, null=True)
