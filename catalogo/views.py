from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import FormularioProduto, FormularioPreco
from .models import Catalogo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class CatalogoListar(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Catalogo
    template_name = 'catalogo.html'
    # def lista_produtos(request):
    #     catalogo = Catalogo.objects.all()
    #     return render(request, 'catalogo.html', {'catalogo': catalogo})


def cadastra_produto(request):
    if request.method == 'POST':
        formulario_produto = FormularioProduto(request.POST or None)
        formulario_preco = FormularioPreco(request.POST or None)
        if all([formulario_produto.is_valid(), formulario_preco.is_valid()]):
            preco = formulario_preco.save()
            produto = formulario_produto.save(commit=False)
            produto.id_preco = preco
            produto.save()
            msg = 'Sucesso ao salvar produto e preco'
            return redirect('catalogo')
    else:
        formulario_produto = FormularioProduto()
        formulario_preco = FormularioPreco()
        msg = 'erro ao salvar produto e preco'
    return render(request, 'formulario_catalogo.html',
                  {'formulario_preco': formulario_preco, 'formulario_produto': formulario_produto})


def atualiza_produto(request, id):
    produto = Catalogo.objects.get(id=id)
    preco = produto.id_preco
    formulario_produto = FormularioProduto(request.POST or None, instance=produto)
    formulario_preco = FormularioPreco(request.POST or None, instance=preco)
    if all([formulario_produto.is_valid(), formulario_preco.is_valid()]):
        preco = formulario_preco.save()
        produto = formulario_produto.save(commit=False)
        produto.id_preco = preco
        produto.save()
        return redirect('catalogo')
    return render(request, 'formulario_catalogo.html',
                  {'produto': produto, 'formulario_preco': formulario_preco, 'formulario_produto': formulario_produto})


def deletar_produto(request, id):
    produto = Catalogo.objects.get(id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('catalogo')
    return render(request, 'confirmar_del_prod.html', {'produto': produto})
