from django import forms
from .models import Tarefa


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa #Indica o modelo associado ao formulário
        fields = ['titulo', 'descricao', 'etiquetas'] #Campos do modelo a serem incluidos no formulário
        

