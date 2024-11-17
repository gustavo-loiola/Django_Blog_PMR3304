from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import Noticia, Comment, HistoricoAcesso
from .forms import NoticiaForm, CommentForm

# View para exibir detalhes de uma notícia e registrar o acesso no histórico
class NoticiaDetalheView(DetailView):
    model = Noticia
    template_name = 'noticias/detail.html'
    context_object_name = 'noticia'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(noticia=self.object).order_by('-data_postagem')
        context['form'] = CommentForm()
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            noticia = self.get_object()
            # Cria o histórico com o URL da notícia
            HistoricoAcesso.objects.create(
                usuario=request.user,
                noticia=noticia,
                url=self.request.build_absolute_uri(reverse('noticias:detalhe', kwargs={'pk': noticia.pk}))
            )
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
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

# View para buscar notícias
def busca_noticias(request):
    query = request.GET.get('query', '')
    noticias_encontradas = Noticia.objects.filter(titulo__icontains=query) if query else Noticia.objects.all()
    context = {
        'lista_noticias': noticias_encontradas,
        'query': query
    }
    return render(request, 'noticias/search.html', context)

# View para criar uma nova notícia (apenas para usuários logados)
class CriarNoticiaView(LoginRequiredMixin, CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'noticias/create.html'
    login_url = 'noticias:login'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Notícia publicada com sucesso!")
        return response

    def get_success_url(self):
        return reverse_lazy('noticias:detalhe', kwargs={'pk': self.object.pk})

# View para atualizar uma notícia
class AtualizarNoticiaView(LoginRequiredMixin, UpdateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'noticias/update.html'
    login_url = 'noticias:login'

    def form_valid(self, form):
        messages.success(self.request, "Notícia atualizada com sucesso!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('noticias:listar')

# View para excluir uma notícia com confirmação
class ExcluirNoticiaView(LoginRequiredMixin, DeleteView):
    model = Noticia
    template_name = 'noticias/delete.html'
    success_url = reverse_lazy('noticias:listar')
    login_url = 'noticias:login'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Notícia excluída com sucesso!")
        return super().delete(request, *args, **kwargs)

# View para exibir o histórico de notícias acessadas pelo usuário
class HistoricoAcessoView(LoginRequiredMixin, ListView):
    model = HistoricoAcesso
    template_name = 'noticias/historico.html'
    context_object_name = 'historico_acesso'
    login_url = 'noticias:login'

    def get_queryset(self):
        return HistoricoAcesso.objects.filter(usuario=self.request.user).order_by('-data_acesso')

# View para registrar um novo usuário
class RegistroView(CreateView):
    form_class = UserCreationForm
    template_name = 'noticias/registro.html'
    success_url = reverse_lazy('noticias:listar')
