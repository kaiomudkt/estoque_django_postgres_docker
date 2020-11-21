from django import forms
from .models import Catalogo, Preco, Fornecedor, Lote, ProdutoFornecedor
from django.contrib.auth.models import User
from django.forms import ModelMultipleChoiceField
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelChoiceField
from django import forms


# CATALOGO / PRODUTO
class FornecedorModelChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "%s| %s" % (obj.id, obj.nome)


class CatalogoForm(forms.ModelForm):
    fornecedor = ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Fornecedor.objects.all())

    class Meta:
        model = Catalogo
        # fields = ['nome', 'descricao', 'slug']
        exclude = ('preco',)


class PrecoCreateForm(forms.ModelForm):
    class Meta:
        model = Preco
        fields = ['real', 'dolar']


# FORNECEDOR
class CatalogoModelChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "ID: %s | Produto: %s" % (obj.id, obj.nome)


class FormularioFornecedor(forms.ModelForm):
    catalogo = CatalogoModelChoiceField(queryset=Catalogo.objects.all(), required=False,
                                        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Fornecedor
        fields = '__all__'


# USUARIO
class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise ValidationError("O email {} já está em uso.".format(e))

        return e


class ProdutoFornecedorModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "Produto: %s | Fornecedor: %s" % (obj.fornecedor.nome, obj.produto.nome)


class FormularioLote(forms.ModelForm):
    produto_fornecedor = ProdutoFornecedorModelChoiceField(queryset=ProdutoFornecedor.objects.all())

    class Meta:
        model = Lote
        fields = '__all__'
