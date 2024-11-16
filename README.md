# **Django_Blog_PMR3304**

Projeto que implementa uma aplicação CRUD completa com Django. O sistema permite a criação, edição e remoção de posts diretamente na aplicação, além de implementar funcionalidades para comentários e categorias.

## Funcionalidades

1. **CRUD de Posts**
   - Criação, visualização, atualização e exclusão de posts com Django.
   - Posts exibidos com título, conteúdo e data de postagem.
   - Sistema de templates com template base na pasta `/templates`.

2. **Sistema de Comentários**
   - Cada post pode ter múltiplos comentários, que são exibidos na página individual do post.
   - Possibilidade de adicionar comentários na página do post, vinculados ao autor.

3. **Categorias de Posts**
   - Os posts podem ser organizados em múltiplas categorias.
   - Página de listagem de posts por categorias, com link para cada categoria na página do post.

## Requisitos

- Django (ver versão compatível em `requirements.txt`)
- Banco de dados SQLite (padrão)
- Git para controle de versão e deploy

## Estrutura do Projeto

- `models.py` — Modelos de dados para Post, Comment e Category.
- `views.py` — Lógica de visualização e CRUD de posts, comentários e categorias.
- `urls.py` — Configurações de URL para navegação entre as páginas.
- `templates/` — Templates HTML para layout e exibição de posts e comentários.
- `static/` — Arquivos estáticos para CSS e JavaScript.
