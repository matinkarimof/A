from typing import Any
from django.shortcuts import render , redirect
from . models import Todo
from . forms import TodoForm, updateForm
from django.contrib import messages

def home(request:Any):
    todos = Todo.objects.all()
    return render(request, template_name='home/index.html' , context={'todos': todos})


def detail(request:Any , todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, template_name='home/detail.html' , context={'todo': todo})



def create(request: Any):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            todo = Todo.objects.create(
                title=cd['title'],
                content=cd['content'],
            )
            messages.success(request, 'Created successfully', extra_tags='success')
            return redirect('home')
            return redirect('detail', todo.id)
    else:
        form = TodoForm()
    return render(request,'home/create.html',{'form': form})


def update(request: Any, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = updateForm(instance=todo, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated successfully', extra_tags='success')
            return redirect('detail', todo_id)
        return render(request, 'home/update.html', {'form': form})
    form = updateForm(instance=todo)
    return render(request,'home/update.html',{'form': form})



def delete(request: Any, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    messages.success(request, 'Deleted successfully', extra_tags='success')
    return redirect('home')