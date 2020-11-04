from django import forms
from .models import Catalogo
from .models import Preco
from fornecedor.models import Fornecedor
from django.forms import ModelMultipleChoiceField

class FornecedorModelChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "%s| %s" % (obj.id, obj.nome)

class FormularioProduto(forms.ModelForm):
    fornecedor = FornecedorModelChoiceField(queryset=Fornecedor.objects.all())
    class Meta:
        model = Catalogo
        fields = ['nome', 'descricao', 'slug']
        # exclude = ('id_preco',)


class FormularioPreco(forms.ModelForm):
    class Meta:
        model = Preco
        fields = ['real', 'dolar']
        # fields = '__all__'
