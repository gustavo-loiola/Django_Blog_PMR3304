from datetime import datetime, timedelta

# Definindo a classe Categoria
class Categoria:
    def __init__(self, nome):
        self.nome = nome

# Definindo a classe Noticia
class Noticia:
    def __init__(self, id, titulo, data, noticia_url, conteudo, categorias):
        self.id = id
        self.titulo = titulo
        self.data = data
        self.noticia_url = noticia_url
        self.conteudo = conteudo
        self.categorias = categorias

# Instâncias de categorias fictícias
categoria_tecnologia = Categoria("Tecnologia")
categoria_ciencia = Categoria("Ciência")
categoria_politica = Categoria("Política")
categoria_entretenimento = Categoria("Entretenimento")
categoria_esportes = Categoria("Esportes")
categoria_saude = Categoria("Saúde")

# Lista de notícias fictícias como objetos Noticia
noticias = [
    Noticia(
        id=1,
        titulo="Descoberta Revolucionária na Inteligência Artificial",
        data=datetime.now() - timedelta(days=2, hours=5),
        noticia_url="https://via.placeholder.com/150",
        conteudo="Pesquisadores revelaram uma descoberta revolucionária na área de inteligência artificial que promete transformar indústrias ao redor do mundo.",
        categorias=[categoria_tecnologia, categoria_ciencia]
    ),
    Noticia(
        id=2,
        titulo="Eleições 2024: Debate entre Candidatos",
        data=datetime.now() - timedelta(days=1, hours=3),
        noticia_url="https://via.placeholder.com/150",
        conteudo="No último debate, os candidatos discutiram temas como saúde, educação e segurança pública.",
        categorias=[categoria_politica]
    ),
    Noticia(
        id=3,
        titulo="Novo Lançamento no Cinema Mundial",
        data=datetime.now() - timedelta(hours=15),
        noticia_url="https://via.placeholder.com/150",
        conteudo="O aguardado filme da famosa série de ficção científica estreou mundialmente, arrecadando milhões em seu primeiro dia.",
        categorias=[categoria_entretenimento]
    ),
    Noticia(
        id=4,
        titulo="A Evolução da Tecnologia em 2024",
        data=datetime.now() - timedelta(days=5),
        noticia_url="https://via.placeholder.com/150",
        conteudo="Com avanços nas áreas de IA, robótica e computação quântica, 2024 promete ser um ano de transformações tecnológicas.",
        categorias=[categoria_tecnologia, categoria_ciencia]
    ),
    Noticia(
        id=5,
        titulo="Vacinas Recentes Mostram Progresso em Saúde Global",
        data=datetime.now() - timedelta(days=7, hours=6),
        noticia_url="https://via.placeholder.com/150",
        conteudo="Novas vacinas para doenças complexas estão mostrando resultados promissores.",
        categorias=[categoria_saude, categoria_ciencia]
    ),
    Noticia(
        id=6,
        titulo="O Impacto das Olimpíadas na Economia",
        data=datetime.now() - timedelta(days=10),
        noticia_url="https://via.placeholder.com/150",
        conteudo="As Olimpíadas trouxeram grandes benefícios econômicos para a cidade-sede, com o turismo em alta.",
        categorias=[categoria_esportes, categoria_politica]
    ),
]

# Função para retornar as notícias
def obter_noticias():
    return noticias
