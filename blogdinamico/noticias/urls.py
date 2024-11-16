from django.urls import path
from . import views

app_name = 'noticias'
urlpatterns = [
    path('', views.lista_noticias, name='index'),
    path('<int:noticia_id>/', views.detalhe, name='detail'),
    path('busca/', views.busca_noticias, name='search'),
    path('criar/', views.cria_noticia, name='create'),
]

'''
    path('nova/', views.nova_noticia, name='nova_noticia'),
    path('editar/<int:noticia_id>/', views.editar_noticia, name='editar_noticia'),
    path('deletar/<int:noticia_id>/', views.deletar_noticia, name='deletar_noticia'),
    path('comentar/<int:noticia_id>/', views.comentar, name='comentar'),
    path('deletar_comentario/<int:comentario_id>/', views.deletar_comentario, name='deletar_comentario'),'
'''