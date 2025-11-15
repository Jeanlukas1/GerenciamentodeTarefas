from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarefa

from django.shortcuts import render
from .models import Tarefa # Certifique-se que Tarefa está sendo importada

# Create your views here.
def main(request):
    
    # 1. Buscamos TODAS as tarefas do banco de dados
    todas_as_tarefas = Tarefa.objects.all()

    # 2. Criamos o "contexto", que é um dicionário
    # A CHAVE (à esquerda) é o nome que o HTML vai usar: "lista_de_tarefas"
    # O VALOR (à direita) é a variável do Python: todas_as_tarefas
    context = {
        "lista_de_tarefas": todas_as_tarefas,
    }

    # 3. Enviamos o 'context' para o template
    return render(request, "index.html", context)