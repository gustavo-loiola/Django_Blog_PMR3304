from django.urls import path
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
]
