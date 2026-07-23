from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


LISTA_CATEGORIAS = (
    ('ANALISES', 'Análises de dados'),
    ('PROGRAMACAO', 'Lógica e programação'),
    ('APRESENTACAO', 'Apresentação impressionadora'),
    ('OUTROS', 'Outros'),
)

# Create your models here.
class Filme(models.Model):
    thumb = models.ImageField(upload_to='thumb_filmes')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    quantidade_view = models.IntegerField(default=0)
    categoria = models.CharField(max_length=20, choices= LISTA_CATEGORIAS)
    data_criacao = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.titulo


class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name= 'episodios', on_delete= models.CASCADE)
    titulo = models.CharField(max_length=100)
    link_video = models.URLField()

    def __str__(self):
        return self.filme.titulo + ' - ' + self.titulo


class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")