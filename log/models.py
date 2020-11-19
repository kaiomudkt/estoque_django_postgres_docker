from django.contrib.auth.models import User
from django.db import models


class Log(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_tabela = models.CharField(max_length=50, null=True)
    id_tupla = models.CharField(max_length=50, null=True)
    metodo = models.CharField(max_length=50, null=True)
    data = models.DateTimeField(auto_now_add=True)

class LogCatalogo(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_tabela = models.CharField(max_length=50, null=True)
    id_tupla = models.CharField(max_length=50, null=True)
    metodo = models.CharField(max_length=50, null=True)
    data = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    id_preco = models.CharField(max_length=50, null=True)

class LogFornecedor(models.Model):
    id_tupla = models.CharField(max_length=50, null=True)
    metodo = models.CharField(max_length=50, null=True)
    data = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255)
    catalogo = models.CharField(max_length=50, null=True)