from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    frase = "Hello World"
    return HttpResponse(frase)

def add(request):
    return HttpResponse("Adicionando uma nova tarefa ao sistema...")

def remove(request):
    return HttpResponse("Removendo tarefas")

def edit(request):
    return HttpResponse("Editando tarefa")

def search(request):
    return HttpResponse("Buscando tarefas")
    