from django import forms
from .models import Lote

class FormularioLote(forms.ModelForm):
    class Meta:
        model = Lote
        #fields = ['data']
        exclude = ('data',)

