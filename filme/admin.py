from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Filme, Episodio, Usuario


# Customização do Painel de Usuários
class UsuarioAdmin(UserAdmin):
    # Copia os campos padrão do UserAdmin e adiciona a seção de Histórico
    fieldsets = tuple(UserAdmin.fieldsets) + (
        ('Histórico', {'fields': ('filmes_vistos',)}),  # A vírgula depois de 'filmes_vistos' é fundamental!
    )


# Registro dos modelos no Django Admin
admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UsuarioAdmin)