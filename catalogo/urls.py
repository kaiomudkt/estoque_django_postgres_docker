from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CatalogoDeletar, CatalogoListar, CatalogoCadastrar, CatalogoAtualizar
from .views import FornecedorDeletar, FornecedorListar, FornecedorCadastrar, FornecedorAtualizar
from .views import UsuarioCreate, PerfilUpdate

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='home.html'), name="home"),

    path('usuario/login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('usuario/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('usuario/registrar/', UsuarioCreate.as_view(), name='registrar_usuario'),
    path('usuario/atualizar/', PerfilUpdate.as_view(), name='atualizar_usuario'),

    path('catalogo/', CatalogoListar.as_view(), name='lista_catalogo'),
    path('catalogo/cadastrar', CatalogoCadastrar.as_view(), name='cadastra_produto'),
    path('catalogo/atualizar<int:id>/', CatalogoAtualizar.as_view(), name='atualiza_produto'),
    path('catalogo/deletar<int:id>/', CatalogoDeletar.as_view(), name='deletar_produto'),

    path('fornecedores/', FornecedorListar.as_view(), name='lista_fornecedores'),
    path('fornecedor/cadastrar', FornecedorCadastrar.as_view(), name='cadastra_fornecedor'),
    path('fornecedor/atualizar<int:id>/', FornecedorAtualizar.as_view(), name='atualiza_fornecedor'),
    path('fornecedor/deletar<int:id>/', FornecedorDeletar.as_view(), name='deletar_fornecedor'),
]
