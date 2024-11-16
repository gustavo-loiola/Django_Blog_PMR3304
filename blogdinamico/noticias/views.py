from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Noticia, Comment
from .forms import NoticiaForm, CommentForm

# View para exibir detalhes de uma notícia e seus comentários
class NoticiaDetalheView(DetailView):
    model = Noticia
    template_name = 'noticias/detail.html'
    context_object_name = 'noticia'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Busca os comentários da notícia e ordena do mais recente ao mais antigo
        context['comments'] = Comment.objects.filter(noticia=self.object).order_by('-data_postagem')
        # Inclui o formulário de comentário no contexto
        context['form'] = CommentForm()
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        # Busca a notícia atual
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.noticia = self.object
            comentario.autor = request.user
            comentario.save()
            messages.success(request, "Comentário adicionado com sucesso!")
            return redirect('noticias:detalhe', pk=self.object.pk)
        return self.get(request, *args, **kwargs)

# View para listar as notícias
class ListaNoticiasView(ListView):
    model = Noticia
    template_name = 'noticias/index.html'
    context_object_name = 'lista_noticias'

# View para buscar notícias (mantida como view funcional)
def busca_noticias(request):
    query = request.GET.get('query', '')  # Obtém a query diretamente
    noticias_encontradas = Noticia.objects.filter(titulo__icontains=query) if query else Noticia.objects.all()
    
    context = {
        'lista_noticias': noticias_encontradas,
        'query': query  # Inclui a query no contexto para exibição no formulário
    }
    return render(request, 'noticias/search.html', context)

# View para criar uma nova notícia
class CriarNoticiaView(CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'noticias/create.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Notícia publicada com sucesso!")
        return response

    def get_success_url(self):
        return reverse_lazy('noticias:detalhe', kwargs={'pk': self.object.pk})

# View para atualizar uma notícia
class AtualizarNoticiaView(UpdateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'noticias/update.html'

    def form_valid(self, form):
        messages.success(self.request, "Notícia atualizada com sucesso!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('noticias:listar')

# View para excluir uma notícia com confirmação
class ExcluirNoticiaView(DeleteView):
    model = Noticia
    template_name = 'noticias/delete.html'
    success_url = reverse_lazy('noticias:listar')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Notícia excluída com sucesso!")
        return super().delete(request, *args, **kwargs)
