from django.shortcuts import render

from .models import LogCatalogo, LogLote, LogPreco, LogFornecedor, LogProdutoFornecedor


def logs(request):
    logs_catalogos = LogCatalogo.objects.all()
    logs_lote = LogLote.objects.all()
    logs_preco = LogPreco.objects.all()
    logs_fornecedor = LogFornecedor.objects.all()
    logs_produto_fornecedor = LogProdutoFornecedor.objects.all()

    return render(request, 'lista_logs.html', {'logs_catalogos': logs_catalogos, 'logs_lote': logs_lote,
                                               'logs_preco': logs_preco, 'logs_fornecedor': logs_fornecedor,
                                               'logs_produto_fornecedor': logs_produto_fornecedor})


def logs_id(request, id):
    logs_catalogos = LogCatalogo.Objects.get(id=id)
    return render(request, 'lista_logs.html', {'logs': logs})
