from django import forms
from .models import Catalogo

class FormularioProduto(forms.ModelForm):
    class Meta:
        model = Catalogo
        fields = ['nome', 'descricao', 'id_preco']
