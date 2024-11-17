from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

# Model de Categoria
class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

# Model de Notícia
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.TextField(max_length=300)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)
    noticia_url = models.URLField(max_length=200)
    categorias = models.ManyToManyField(Categoria, related_name='noticias')

    def __str__(self):
        return self.titulo

# Model de Comentário
class Comment(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comments')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário de {self.autor} na notícia {self.noticia}'

# Model de Histórico de Acesso
class HistoricoAcesso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    data_acesso = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=300, blank=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.noticia.titulo} em {self.data_acesso}'

    def save(self, *args, **kwargs):
        # Atualiza o campo URL com o caminho completo da notícia
        if not self.url:
            self.url = self.get_noticia_url()
        super().save(*args, **kwargs)

    def get_noticia_url(self):
        # Obtém o caminho absoluto para a notícia
        return reverse('noticias:detalhe', kwargs={'pk': self.noticia.pk})

# Model de Histórico de Busca
class HistoricoBusca(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    termo = models.CharField(max_length=100)
    data_busca = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Busca por '{self.termo}' de {self.usuario.username} em {self.data_busca}"
