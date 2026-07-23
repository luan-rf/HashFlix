from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .models import Filme, Usuario
from .forms import CriarContaForm, HomeForm



#------ FUNCTION BASED VIEW (FBV) ------#
# def homepage(request):
#     return render(request, "homepage.html")


#------ CLASS BASED VIEW (CBV) ------#
class Homepage(FormView):
    template_name = 'homepage.html'
    form_class = HomeForm

    def get(self, request, *args, **kwargs):
        # checar se o usuário está logado
        if request.user.is_authenticated: # se há usuário logado, redireciona para a página de filmes
            return redirect('filme:homefilmes')
        else: # redireciona para a home padrão com opção de login
            return super().get(request, *args, **kwargs )


    # tratamento com o formulario da pagina homepage
    def get_success_url(self):
        # procura pelo email que foi inserido no metodo post do formulario da homepage
        email = self.request.POST.get('email')
        # filtra a informação no banco de dados, conforme o que foi escrito no post
        usuario = Usuario.objects.filter(email=email)
        # se houver usuário cadastrado com o email informado
        if usuario:
            # retorna a pagina (https) do login para ser realizado
            return reverse('filme:login')
        else:
            # retorna para a pagina (https) para criar conta
            return reverse('filme:criarconta')


class HomeFilmes(LoginRequiredMixin, ListView):
    template_name = 'homefilmes.html'
    # object_list -> nome que o ListView da para a lista de objetos do modelo que foi passado
    model = Filme


class DetalheFilme(LoginRequiredMixin, DetailView):
    template_name = 'detalhes_filme.html'
    # object -> 1 item do modelo  (variavel que vai pro html)
    model = Filme


    def get(self, request, *args, **kwargs):
        # descobrir qual filme está sendo acesado
        filme = self.get_object()
        # adiciona 1 na view
        filme.quantidade_view += 1
        # salva o bd do filme com a alteração que foi feita
        filme.save()
        # registra o filme na lista de filmes_vistos do usuário
        usuario = request.user
        if usuario.is_authenticated:
            usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs) # redireciona o usuário para o link final


    def get_context_data(self, **kwargs):
        context = super(DetalheFilme, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:3]
        context['filmes_relacionados'] = filmes_relacionados
        return context


class BarraPesquisa(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Filme

    def get_queryset(self):
        pesquisa = self.request.GET.get('query')
        # editar o object_list
        if pesquisa:
            # caso tenha o campo preenchido, vamos alterar o object list que o listview encaminha originalmente
            # filtrando o campo do FILME pelo titulo que contenha a pesquisa do usuário que foi pego no GET
            object_list = self.model.objects.filter(titulo__icontains=pesquisa)
            return object_list
        else:
            return None


class EditaPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'edita_perfil.html'
    model = Usuario
    # quais campos o usuário vai conseguir alterar (por conta do UpdateView)
    # campos herdados do AbstractUser que são usados para os usuários que são criados
    fields = ['first_name', 'last_name', 'email']


    def get_success_url(self) -> str:
        return reverse('filme:homefilmes')


class CriarConta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')


class Paginalogout(LogoutView):
    template_name = "logout.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)