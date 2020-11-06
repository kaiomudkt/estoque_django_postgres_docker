from django.shortcuts import render

from .models import Log


def logs(request):
    logs = Log.objects.all()
    return render(request, 'lista_logs.html', {'logs': logs})


def logs_id(request, id):
    logs = Log.Objects.get(id=id)
    return render(request, 'lista_logs.html', {'logs': logs})
