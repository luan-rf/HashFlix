from django.urls import path, reverse_lazy
from .views import Homepage, HomeFilmes, DetalheFilme, BarraPesquisa, EditaPerfil, CriarConta
from django.contrib.auth import views as auth_view


app_name = 'filme'
urlpatterns = [
    path('', Homepage.as_view(), name= 'homepage'),
    path('filmes/', HomeFilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', DetalheFilme.as_view(), name= 'detalhesfilme'),
    path('pesquisa/', BarraPesquisa.as_view(), name='pesquisa'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('edita_perfil/<int:pk>', EditaPerfil.as_view(), name='edita_perfil'),
    path('criarconta/', CriarConta.as_view(), name='criarconta'),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='edita_perfil.html',
                                                             success_url= reverse_lazy('filme:homefilmes')),
                                                            name='mudarsenha'),

]