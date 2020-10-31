from django.db import models
from django.contrib.auth.models import User

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_tabela = 1
    id_tupla = 1
    metodo = 'atualizar'
    data = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)