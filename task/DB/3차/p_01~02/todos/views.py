from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)

def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TodoForm(request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.author = request.user
                todo.save()
                return redirect('todos:index')
        else:
            form = TodoForm()
        context = {
            'form': form,
        }
        return render(request, 'todos/create.html', context)
    else:
        return redirect('accounts:login')


def toggle(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == todo.author:
            if request.method == 'POST':
                if todo.completed:
                    todo.completed = 0
                else:
                    todo.completed = 1
                todo.save()
        return redirect('todos:index')
    else:
        return redirect('accounts:login')


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == todo.author:
            if request.method == 'POST':
                todo.delete()
        return redirect('todos:index')
    else:
        return redirect('accounts:login')

