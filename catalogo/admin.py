from django.contrib import admin

from .models import Catalogo, Preco, Fornecedor, ProdutoFornecedor, Lote, Perfil

admin.site.register(Catalogo)
admin.site.register(Preco)
admin.site.register(Fornecedor)
admin.site.register(ProdutoFornecedor)
admin.site.register(Lote)
admin.site.register(Perfil)
