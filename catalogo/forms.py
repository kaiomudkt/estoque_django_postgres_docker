from django import forms
from .models import Catalogo
from .models import Preco

class FormularioProduto(forms.ModelForm):
    class Meta:
        model = Catalogo
        #fields = ['nome', 'descricao', 'id_preco']
        exclude = ('id_preco',)


class FormularioPreco(forms.ModelForm):
    class Meta:
        model = Preco
        fields = ['real', 'dolar']
