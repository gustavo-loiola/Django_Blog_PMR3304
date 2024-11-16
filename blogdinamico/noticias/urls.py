from django.urls import path
from . import views

app_name = 'noticias'
urlpatterns = [
    path('', views.lista_noticias, name='listar'),  # Listar todas as notícias
    path('<int:noticia_id>/', views.detalhe, name='detalhe'),  # Exibir detalhes de uma notícia
    path('busca/', views.busca_noticias, name='buscar'),  # Buscar notícias
    path('criar/', views.cria_noticia, name='criar'),  # Criar uma nova notícia
    path('atualizar/<int:noticia_id>/', views.atualizar_noticia, name='atualizar'),  # Atualizar uma notícia
    path('excluir/<int:noticia_id>/', views.excluir_noticia, name='excluir'),  # Excluir uma notícia com confirmação
]