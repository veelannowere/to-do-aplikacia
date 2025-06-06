from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login as auth_login
from .models import Task, Todo
from .forms import TaskForm
from django.db import models


def index(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task added successfully!")
            return redirect('todo')
    else:
        form = TaskForm()
    
    # Get current sort direction from session or set default
    sort_direction = request.session.get('sort_direction', 'desc')
    
    item_list = Todo.objects.all()
    if request.GET.get('sort') == 'date':
        # Toggle sort direction
        if sort_direction == 'desc':
            item_list = item_list.order_by('date')
            request.session['sort_direction'] = 'asc'
        else:
            item_list = item_list.order_by('-date')
            request.session['sort_direction'] = 'desc'
    else:
        item_list = item_list.order_by('-date')

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
        "sort_direction": sort_direction
    }
    return render(request, 'todo/index.html', page)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')

def login_view(request):
    # ...existing code...
    if user is not None:
        messages.get_messages(request).used = True  # Clear any existing messages
        messages.success(request, 'Hi Admin, welcome back!')
        auth_login(request, user)
        return redirect('todo')
    # ...existing code...
def edit(request, item_id):
    task = get_object_or_404(Todo, id=item_id)
    
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.details = request.POST.get('details')
        task.date = request.POST.get('date')
        task.save()
        return redirect('todo')
    else:
        form = TaskForm(instance=task)
    
    context = {'form': form, 'task': task}
    return render(request, 'todo/edit_task.html', context)

