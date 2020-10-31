from django.shortcuts import render, redirect

from .forms import FormularioLote
from .models import Lote


def lista_lotes(request):
    lotes = Lote.objects.all()
    return render(request, 'lotes.html', {'lotes': lotes})


def cadastra_lote(request):
    if request.method == 'POST':
        formulario = FormularioLote(request.POST or None)
        if formulario.is_valid():
            lote = formulario.save()
            lote.save()
            msg = 'Sucesso ao salvar lote'
            return redirect('lotes')
    else:
        formulario = FormularioLote()
        msg = 'erro ao salvar lote'
    return render(request, 'formulario.html', {'formulario': formulario})


def atualiza_lote(request, id):
    lote = Lote.objects.get(id=id)
    formulario = FormularioLote(request.POST or None, instance=lote)
    if formulario.is_valid():
        formulario.save()
        return redirect('lotes')
    return render(request, 'formulario.html', {'lote': lote, 'formulario': formulario})


def deletar_lote(request, id):
    lote = Lote.objects.get(id=id)
    if request.method == 'POST':
        lote.delete()
        return redirect('lotes')
    return render(request, 'confirmar_del_lote.html', {'lote': lote})
