from django.contrib.auth import views as auth_views
from django.urls import path

from .views import UsuarioCreate, PerfilUpdate

urlpatterns = [
    path('', auth_views.LoginView.as_view(
        template_name='home.html'), name="home"),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),
    path('atualizar-dados/', PerfilUpdate.as_view(), name='atualizar-dados'),
]
