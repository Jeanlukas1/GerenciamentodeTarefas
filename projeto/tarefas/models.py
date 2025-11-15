from django.db import models

# Create your models here.
class Tarefa(models.Model):
    titulo_tarefa = models.CharField(max_length=120)
    descricao_tarefa = models.CharField(max_length=120, default="",)
    data_tarefa = models.DateField(auto_now_add=True)
    
    class Metas:
        oredering = ('title', 'subject_content',)
    