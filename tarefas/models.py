from django.db import models
from django.contrib.auth.models import User

class Etiqueta(models.Model):
    nome = models.CharField(unique=True) #Nome da etiqueta | unique=True garante que não haja etiquetas com nomes duplicados
    cor = models.CharField(default="#000000") #Cor associada à etiqueta, padrão é branco

    def __str__(self):
        return self.nome #retorna o nome da etiqueta como representação string do objeto
    
# Create your models here.
class Tarefa(models.Model):
    titulo = models.CharField(max_length=100) #Titulo da tarefa com limite de 100 caracteres
    descricao = models.TextField(blank=True) #Descrição detralhada da tarefa, pode ser deixada em branco
    concluida = models.BooleanField(default=False) #Indica se a tarefa foi concluida.
    criada_em = models.DateTimeField(auto_now_add=True) #Data e Hora em que a tarefa foi criada
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #Relaciona a tarefa a um usuário específico
    #O Cascade garante que se o usuário for deletado, todas as suas tarefas também serão deletadas.
    #O Protect impediria a deleção do usuário se ele tiver tarefas associadas.
    #O SetNull definiria o campo usuario como nulo se o usuário for deletado, desde que o campo permita nulos.
    etiquetas = models.ManyToManyField(Etiqueta, blank=True) #Relaciona a tarefa a múltiplas etiquetas, pode ser deixada em branco

    class Meta:
        permissions = [
            ("can_view_all_tarefas", "Can view tasks from all users")
        ]

    def __str__(self):
        return self.titulo #retorna o titulo da tarefa como representação string do objeto
    
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE) #Relaciona o perfil a um usuário específico
    bio = models.TextField(blank=True) #Biografia do usuário, pode ser deixada em branco
    tema = models.BooleanField(default=False) #Tema preferido do usuário, padrão é False (pode representar tema claro ou escuro)

    def __str__(self):
        return f"Perfil de {self.usuario.username}" #retorna o nome de usuário como representação string do objeto
    
