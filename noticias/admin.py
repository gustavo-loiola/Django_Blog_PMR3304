from django.contrib import admin
from .models import Noticia, Categoria, Comment

# Register your models here.
admin.site.register(Noticia)
admin.site.register(Categoria)
admin.site.register(Comment)
