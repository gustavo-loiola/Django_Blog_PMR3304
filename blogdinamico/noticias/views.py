from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Noticia
from .forms import NoticiaForm

# View para exibir detalhes de uma notícia
def detalhe(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    context = {"noticia": noticia}
    return render(request, 'noticias/detail.html', context)

# View para listar as notícias
def lista_noticias(request):
    lista_noticias = Noticia.objects.all()
    context = {"lista_noticias": lista_noticias}
    return render(request, 'noticias/index.html', context)

# View para buscar notícias
def busca_noticias(request):
    query = request.GET.get('query', '')  # Obtém a query diretamente
    noticias_encontradas = Noticia.objects.filter(titulo__icontains=query) if query else Noticia.objects.all()
    
    context = {
        'lista_noticias': noticias_encontradas,
        'query': query  # Inclui a query no contexto para exibição no formulário
    }
    return render(request, 'noticias/search.html', context)

# View para criar uma nova notícia
def cria_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Notícia publicada com sucesso!")
            return redirect('noticias:listar')
    else:
        form = NoticiaForm()
    return render(request, 'noticias/create.html', {'form': form})

# View para atualizar uma notícia
def atualizar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            messages.success(request, "Notícia atualizada com sucesso!")
            return redirect('noticias:listar')
    else:
        form = NoticiaForm(instance=noticia)
    return render(request, 'noticias/atualizar_noticia.html', {'form': form})

# View para excluir uma notícia com confirmação
def excluir_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    if request.method == 'POST':
        noticia.delete()
        messages.success(request, "Notícia excluída com sucesso!")
        return redirect('noticias:listar')
    return render(request, 'noticias/excluir_noticia.html', {'noticia': noticia})
