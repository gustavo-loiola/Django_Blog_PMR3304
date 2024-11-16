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

def busca_noticias(request):
    query = request.GET.get('query', '').lower()  # Obtém a query, converte para minúsculas para busca insensível
    noticias_encontradas = []
    if query:
        noticias = obter_noticias()
        noticias_encontradas = [noticia for noticia in noticias if query in noticia.titulo.lower()]

    context = {
        'lista_noticias': noticias_encontradas,
        'query': query  # Inclui a query no contexto para exibição no formulário
    }
    return render(request, 'noticias/search.html', context)