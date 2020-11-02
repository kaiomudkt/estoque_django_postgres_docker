from django import forms
from django.forms import ModelMultipleChoiceField
from catalogo.models import Catalogo
from fornecedor.models import Fornecedor

class CatalogoModelChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "%s| %s" % (obj.id, obj.nome)


class FormularioFornecedor(forms.ModelForm):
    catalogo = CatalogoModelChoiceField(queryset=Catalogo.objects.all())

    class Meta:
        model = Fornecedor
        #fields = ('nome','cnpj',)
        fields = '__all__'
        # exclude = ('catalogo', )
