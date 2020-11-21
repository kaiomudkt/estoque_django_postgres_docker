from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals


class Perfil(models.Model):
    nome_completo = models.CharField(max_length=50, null=True)
    cpf = models.CharField(max_length=14, null=True, verbose_name="CPF")
    telefone = models.CharField(max_length=16, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)


class Preco(models.Model):
    dolar = models.DecimalField(max_digits=9, decimal_places=2)
    real = models.DecimalField(max_digits=9, decimal_places=2)


class Catalogo(models.Model):
    nome = models.CharField(max_length=255)
    # slug = models.SlugField(max_length=255, unique=True)
    preco = models.OneToOneField(Preco, on_delete=models.SET_NULL, null=True)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255)
    catalogo = models.ManyToManyField(Catalogo, through='ProdutoFornecedor', through_fields=('produto', 'fornecedor'),
                                      blank=True)

    def __str__(self):
        return self.nome


class ProdutoFornecedor(models.Model):
    fornecedor = models.ForeignKey(Catalogo, on_delete=models.CASCADE)
    produto = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)


class Lote(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    quantidade = models.IntegerField()
    produto_fornecedor = models.ForeignKey(ProdutoFornecedor, on_delete=models.CASCADE)


def update_fornecedor(sender, instance, created, **kwargs):
    fornecedores_info = getattr(instance, '_catalogo', None)
    if fornecedores_info is not None:
        fornecedor_salvos = []
        produto_fornecedor = ProdutoFornecedor.objects.filter(produto__catalogo=instance)
        for fornecedor in produto_fornecedor:
            if fornecedor.fornecedor == instance:
                fornecedor_salvos.append(fornecedor.produto)
        if fornecedor_salvos:
            for fornecedor in fornecedores_info:
                if fornecedor not in fornecedor_salvos:
                    fornecedor.catalogo.add(instance)
            for fornecedor in fornecedor_salvos:
                if fornecedor not in fornecedores_info:
                    prod_del = ProdutoFornecedor.objects.filter(fornecedor__fornecedor__exact=fornecedor)
                    for prod in prod_del:
                        if prod.produto == fornecedor and prod.fornecedor == instance:
                            prod.delete()
        else:
            for fornecedor in fornecedores_info:
                if fornecedor not in produto_fornecedor:
                    fornecedor.catalogo.add(instance)


signals.post_save.connect(receiver=update_fornecedor, sender=Catalogo)
