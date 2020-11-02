from django.shortcuts import render, redirect

from .forms import FormularioFornecedor
from fornecedor.models import Fornecedor

def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedores.html', {'fornecedores': fornecedores})


def cadastra_fornecedor(request):
    if request.method == 'POST':
        formulario = FormularioFornecedor(request.POST or None)
        if formulario.is_valid():
            fornecedor = formulario.save()
            fornecedor.save()
            msg = 'Sucesso ao salvar fornecedor'
            return redirect('fornecedores')
    else:
        formulario = FormularioFornecedor()
        msg = 'erro ao salvar fornecedor'
    return render(request, 'formulario_catalogo.html', {'formulario': formulario})


def atualiza_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    formulario = FormularioFornecedor(request.POST or None, instance=fornecedor)
    if formulario.is_valid():
        formulario.save()
        return redirect('fornecedores')
    return render(request, 'formulario_catalogo.html', {'fornecedir': fornecedor, 'formulario': formulario})


def deletar_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('fornecedores')
    return render(request, 'confirmar_del_fornecedor.html', {'fornecedor': fornecedor})
