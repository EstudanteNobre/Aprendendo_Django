from django.contrib import admin
from .models import Tarefa, Etiqueta, Perfil

# Register your models here.

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'criada_em') #   Exibe essas colunas na lista de tarefas

admin.site.register(Tarefa, TarefaAdmin)

# Classe de Etiquetas
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cor']

admin.site.register(Etiqueta, EtiquetaAdmin)

# Classe de Perfil do Usuario
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['bio' , 'tema']
    
admin.site.register(Perfil, PerfilAdmin)