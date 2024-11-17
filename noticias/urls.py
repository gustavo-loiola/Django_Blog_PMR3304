from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'noticias'
urlpatterns = [
    path('', views.ListaNoticiasView.as_view(), name='listar'),
    path('<int:pk>/', views.NoticiaDetalheView.as_view(), name='detalhe'),
    path('busca/', views.busca_noticias, name='buscar'),
    path('criar/', views.CriarNoticiaView.as_view(), name='criar'),
    path('atualizar/<int:pk>/', views.AtualizarNoticiaView.as_view(), name='atualizar'),
    path('excluir/<int:pk>/', views.ExcluirNoticiaView.as_view(), name='excluir'),
    path('historico/', views.HistoricoAcessoView.as_view(), name='historico_acesso'),
    path('login/', auth_views.LoginView.as_view(template_name='noticias/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='noticias:listar'), name='logout'),
    path('registro/', views.RegistroView.as_view(), name='registro'),
    path('categorias/', views.CategoriaListView.as_view(), name='lista_categorias'),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='detalhe_categoria'),
]