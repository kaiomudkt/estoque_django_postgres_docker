from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Óla mundo, catalogo.")

def cadastra_produto(request):
    catalogo = Catalogo.Objects.all()
    return render(request, 'catalogo.html', {'catalogo': catalogo})