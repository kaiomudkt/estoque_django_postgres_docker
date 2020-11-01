from django.http import HttpResponse


def index(request):
    return HttpResponse(
        """
        path('', include('polls.urls')), <br>
        path('catalogo/', include('catalogo.urls')),<br>
        path('log/', include('log.urls')),<br>
        path('lote/', include('lote.urls')),<br>
        path('admin/', admin.site.urls)<br>
        """
    )
