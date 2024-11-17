from django import forms
from .models import Noticia, Categoria, Comment

class NoticiaForm(forms.ModelForm):
    categorias = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Categorias (Escolha até 3)"
    )

    class Meta:
        model = Noticia
        fields = ['titulo', 'resumo', 'conteudo', 'noticia_url', 'categorias']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['texto']
        labels = {'texto': 'Comentário'}
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escreva seu comentário...'}),
        }