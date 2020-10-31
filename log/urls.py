from django.urls import path

from .views import logs, logs_id

urlpatterns = [
    path('', logs, name='logs'),
    path('<int:id>/', logs_id, name='logs_id'),
]
