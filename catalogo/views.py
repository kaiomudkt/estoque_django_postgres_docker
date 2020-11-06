from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .forms import CatalogoForm, PrecoCreateForm, FormularioFornecedor, UsuarioForm
from .models import Catalogo, Preco, Fornecedor, Perfil


# Pagina Inicial
class Home(TemplateView):
    template_name = 'home.html'


# CATALOGO/PRODUTO
class CatalogoListar(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Catalogo
    template_name = 'listar/catalogo.html'


class PrecoCadastrar(CreateView):
    model = Preco
    fields = ['real', 'dolar']


class CatalogoCadastrar(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name = 'formulario.html'
    form_class = CatalogoForm
    model = Catalogo
    second_form_class = PrecoCreateForm
    # fields = ['nome', 'descricao', 'slug']
    success_url = reverse_lazy('lista_catalogo')

    def get_context_data(self, *args, **kwargs):
        context = super(CatalogoCadastrar, self).get_context_data(**kwargs)
        context['preco_form'] = self.second_form_class
        # context = super().get_context_data(*args, **kwargs)
        context['botao'] = "Cadastrar"
        context['titulo'] = "Cadastro novo produto no catalogo"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        return context

    def form_valid(self, form):
        preco_form = PrecoCreateForm(self.request.POST)
        if preco_form.is_valid():
            preco = preco_form.save()
            produto = form.save(commit=False)
            # produto.preco_id = preco.id
            produto.preco = preco
            produto.save()
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
        # return HttpResponseRedirect(self.get_success_url())


class CatalogoAtualizar(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Catalogo
    template_name = 'formulario.html'
    form_class = CatalogoForm
    second_form_class = PrecoCreateForm
    success_url = reverse_lazy('lista_catalogo')
    success_message = 'Sucesso ao atualizar produto do catalogo'

    def get_context_data(self, **kwargs):
        context = super(CatalogoAtualizar, self).get_context_data(**kwargs)
        context['preco_form'] = self.second_form_class(self.request.POST or None, instance=self.object.preco)
        context['botao'] = "Salvar Atualizações"
        context['titulo'] = "Atualizar produto no catalogo"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Catalogo, pk=self.kwargs['id'])
        return self.object

    def form_valid(self, form):
        preco_form = PrecoCreateForm(self.request.POST, instance=self.object.preco)
        if preco_form.is_valid():
            preco = preco_form.save()
            produto = form.save(commit=False)
            produto.preco = preco
            produto.save()
            return HttpResponseRedirect(self.get_success_url())


class CatalogoDeletar(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Catalogo
    template_name = 'confirmar_del.html'
    success_url = reverse_lazy('lista_catalogo')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Catalogo, pk=self.kwargs['id'])
        return self.object


#   FORNECEDOR
class FornecedorListar(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Fornecedor
    template_name = 'listar/fornecedores.html'


class FornecedorAtualizar(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Fornecedor
    template_name = 'formulario.html'
    form_class = FormularioFornecedor
    success_url = reverse_lazy('lista_fornecedores')
    success_message = 'Sucesso ao atualizar fornecedor.'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de fornecedor"
        context['botao'] = "Salvar"
        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Fornecedor, pk=self.kwargs['id'])
        return self.object


class FornecedorCadastrar(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Fornecedor
    template_name = 'formulario.html'
    success_url = reverse_lazy('lista_fornecedores')
    form_class = FormularioFornecedor

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Fornecedor"
        context['botao'] = "Cadastrar Fornecedor"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        return context


class FornecedorDeletar(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Fornecedor
    template_name = 'confirmar_del.html'
    success_url = reverse_lazy('lista_fornecedores')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Fornecedor, pk=self.kwargs['id'])
        return self.object


#  USUARIO
class UsuarioCreate(CreateView):
    template_name = "formulario.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"
        return context


class PerfilUpdate(UpdateView):
    template_name = "formulario.html"
    model = Perfil
    fields = ["nome_completo", "cpf", "telefone"]
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Meus dados pessoais"
        context["botao"] = "Atualizar"
        return context
