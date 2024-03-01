from django.shortcuts import render
from .models import Todo

# Rendering home page
def index(request):
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'index.html', {'todos': todos})


# Creating a new Todo
def create_todo(request):
    title = request.POST.get('title')
    todo = Todo.objects.create(title=title)
    todo.save()
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos})

# Marking completed True
def mark_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = True
    todo.save()
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos})

# Deleting a Todo
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos})