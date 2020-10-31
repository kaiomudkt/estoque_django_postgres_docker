from django import forms
from .models import Preco

class FormularioPreco(forms.ModelForm):
    class Meta:
        model = Preco
        fields = ['real', 'dolar']
