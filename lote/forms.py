from django import forms
from .models import Lote
from django.forms import ModelChoiceField
from catalogo.models import Catalogo
from fornecedor.models import Fornecedor

class ProdutoModelChoiceField (ModelChoiceField):
    def label_from_instance (self, obj):
        return "Produto #%s) %s" % (obj.id, obj.nome)

class FornecedorModelChoiceField (ModelChoiceField):
    def label_from_instance (self, obj):
        return "Fornecedor #%s) %s" % (obj.id, obj.nome)

class FormularioLote(forms.ModelForm):
    produto = ProdutoModelChoiceField(queryset=Catalogo.objects.all())
    fornecedor = FornecedorModelChoiceField(queryset=Fornecedor.objects.all())
    class Meta:
        model = Lote
        #fields = ['quantidade']
        fields = '__all__'
        # exclude = ('data',)

