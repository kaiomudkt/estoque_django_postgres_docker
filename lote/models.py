from django.db import models

class Lote(models.Model):
    quantidade = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
