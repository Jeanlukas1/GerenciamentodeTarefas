from django.urls import path
from tarefas import views

urlpatterns = [
    path('', views.main, name='main'),
]
