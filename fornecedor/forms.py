from django import forms
from django.forms import ModelMultipleChoiceField
from catalogo.models import Catalogo
from .models import Fornecedor


# class CatalogoModelChoiceField(ModelMultipleChoiceField):
#     def label_from_instance(self, obj):
#         return "Produto #%s) %s" % (obj.id, obj.nome)


class FormularioFornecedor(forms.ModelForm):
    # produto = CatalogoModelChoiceField(queryset=Catalogo.objects.all())

    class Meta:
        model = Fornecedor
        # fields = '__all__'
        exclude = ('catalogo', )
