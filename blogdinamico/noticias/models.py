from django.db import models
from django.conf import settings

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.TextField(max_length=300)  
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)
    noticia_url = models.URLField(max_length=200)
    categorias = models.ManyToManyField(Categoria, related_name='noticias')

    def __str__(self):
        return self.titulo
