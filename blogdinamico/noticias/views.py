from django.shortcuts import render
from django.http import HttpResponse
from .temp_data import obter_noticias

# Create your views here.
def detalhe(request, noticia_id):
    context = {"noticia": obter_noticias()[int(noticia_id) - 1]}
    return render(request, 'noticias/detalhe.html', context)

def lista_noticias(request):
    context = {"lista_noticias": obter_noticias()}
    return render(request, 'noticias/index.html', context)