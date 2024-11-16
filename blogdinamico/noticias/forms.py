from django import forms
from .models import Noticia, Categoria

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
