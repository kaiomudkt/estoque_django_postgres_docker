from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Catalogo
from .forms import FormularioProduto


def lista_produtos(request):
    catalogo = Catalogo.objects.all()
    return render(request, 'catalogo.html', {'catalogo': catalogo})


def cadastra_produto(request):
    formulario = FormularioProduto(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('catalogo')
    return render(request, 'formulario.html', {'formulario': formulario})


def atualiza_produto(request, id):
    produto = Catalogo.objects.get(id=id)
    formulario = FormularioProduto(request.POST or None, instance=produto)
    if formulario.is_valid():
        formulario.save()
        return redirect('catalogo')
    return render(request, 'formulario.html', {'formulario': formulario, 'produto': produto})


def deletar_produto(request, id):
    produto = Catalogo.objects.get(id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('catalogo')
    return render(request, 'confirmar_del_prod.html', {'produto': produto})
