from .models import Filme


def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    return {"lista_filmes_recentes": lista_filmes}


def lista_filmes_populares(request):
    lista_filmes = Filme.objects.all().order_by('-quantidade_view')[0:8]
    return {"lista_filmes_populares": lista_filmes}


def filme_destaque(request):
    # .first() retorna o primeiro objeto ou None de forma segura caso a tabela esteja vazia
    filme = Filme.objects.order_by('-data_criacao').first()
    return {"filme_destaque": filme}