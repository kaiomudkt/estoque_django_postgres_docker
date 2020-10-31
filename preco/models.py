from django.db import models


# from catalogo.models import Catalogo


class Preco(models.Model):
    dolar = models.DecimalField(max_digits=9, decimal_places=2)
    real = models.DecimalField(max_digits=9, decimal_places=2)

    # def __unicode__(self):
    #     return '%s' % self.real
    #
    # def __str__(self):
    #     return "% s" % (self.real)
