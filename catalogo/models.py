from django.db import models

# from lote.models import Lote
from preco.models import Preco


class Catalogo(models.Model):
    nome = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    id_preco = models.OneToOneField(Preco, on_delete=models.SET_NULL, null=True)
    descricao = models.TextField()
    # lote = models.ForeignKey(Lote, on_delete=models.CASCADE, related_name='lotes')
