from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
from .temp_data import obter_noticias, Noticia, Categoria

noticias = obter_noticias()

# Mapear as categorias disponíveis
categoria_opcoes = {
    "tecnologia": Categoria("Tecnologia"),
    "ciencia": Categoria("Ciência"),
    "politica": Categoria("Política"),
    "entretenimento": Categoria("Entretenimento"),
    "esportes": Categoria("Esportes"),
    "saude": Categoria("Saúde"),
}

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

def cria_noticia(request):
    if request.method == 'POST':
        # Captura os dados do formulário
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        noticia_url = request.POST.get('noticia_url')
        categorias_selecionadas = request.POST.getlist('categorias')

        # Limitar a seleção a no máximo 3 categorias
        categorias = [categoria_opcoes[c] for c in categorias_selecionadas[:3] if c in categoria_opcoes]

        # Cria uma nova instância de Noticia
        nova_noticia = Noticia(
            id=len(noticias) + 1,  # Exemplo de ID, deve ser gerado pelo banco de dados em produção
            titulo=titulo,
            data=datetime.now(),
            noticia_url=noticia_url,
            conteudo=conteudo,
            categorias=categorias  # Adiciona as categorias selecionadas
        )

        # Adiciona a nova notícia à lista de notícias (somente para este exemplo)
        noticias.append(nova_noticia)

        # Mensagem de sucesso
        messages.success(request, "Notícia publicada com sucesso!")

        # Redireciona para a página de listagem de notícias ou detalhes
        return redirect('noticias:index')

    return render(request, 'noticias/create.html')
