from django.shortcuts import render
from .models import Todo


def home(request):
    return render(request, 'base.html')


def todoList(request):
    qs = Todo.objects.all()
    template_name = 'todoapp/todolist.html'
    context = {'todos':qs }
    return render(request, template_name, context)