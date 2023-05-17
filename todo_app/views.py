# todo_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Todo.objects.create(title=title, description=description)
        return redirect('/')
    return render(request, 'add_todo.html')

def update_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return redirect('/')
    return render(request, 'update_todo.html', {'todo': todo})

def delete_todo(request, pk):
    Todo.objects.get(pk=pk).delete()
    return redirect('/')
