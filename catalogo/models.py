from django.db import models


# from lote.models import Lote


class Preco(models.Model):
    dolar = models.DecimalField(max_digits=9, decimal_places=2)
    real = models.DecimalField(max_digits=9, decimal_places=2)


class Catalogo(models.Model):
    nome = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    preco = models.OneToOneField(Preco, on_delete=models.SET_NULL, null=True)
    descricao = models.TextField()
    # lote = models.ForeignKey(Lote, on_delete=models.CASCADE, related_name='lotes')

    # def __str__(self):
    #     return "%s" % (self.nome)
    def __str__(self):
        return "[{}] {}".format(self.pk, self.nome )
