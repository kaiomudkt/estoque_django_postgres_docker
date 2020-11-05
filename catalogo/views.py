from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .forms import CatalogoForm, PrecoCreateForm
from .models import Catalogo, Preco


class CatalogoListar(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Catalogo
    template_name = 'catalogo.html'
    # def lista_produtos(request):
    #     catalogo = Catalogo.objects.all()
    #     return render(request, 'catalogo.html', {'catalogo': catalogo})


class PrecoCadastrar(CreateView):
    model = Preco
    fields = ['real', 'dolar']


class CatalogoCadastrar(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name = 'formulario_catalogo.html'
    form_class = CatalogoForm
    model = Catalogo
    second_form_class = PrecoCreateForm
    # fields = ['nome', 'descricao', 'slug']
    success_url = reverse_lazy('catalogo')

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
            #produto.preco_id = preco.id
            produto.preco = preco
            produto.save()
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
        #return HttpResponseRedirect(self.get_success_url())


class CatalogoAtualizar(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Catalogo
    template_name = 'formulario_catalogo.html'
    form_class = CatalogoForm
    second_form_class = PrecoCreateForm
    success_url = reverse_lazy('catalogo')
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
        # self.object = get_object_or_404(Catalogo, pk=self.kwargs['id'], usuario=self.request.user)
        return self.object

    def form_valid(self, form):
        preco_form = PrecoCreateForm(self.request.POST, instance=self.object.preco)
        if preco_form.is_valid():
            preco = preco_form.save()
            produto = form.save(commit=False)
            produto.preco = preco
            produto.save()
            return HttpResponseRedirect(self.get_success_url())
            # return super(CatalogoAtualizar, self).form_valid(form)
        # Antes do super não foi criado o objeto nem salvo no banco
        # form.instance.usuario = self.request.user
        # url = super().form_valid(form)
        # return url


def deletar_produto(request, id):
    produto = Catalogo.objects.get(id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('catalogo')
    return render(request, 'confirmar_del_prod.html', {'produto': produto})
