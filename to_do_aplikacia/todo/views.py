from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login as auth_login

from .forms import TodoForm
from .models import Todo

def index(request):
    if not request.user.is_authenticated:  # Opravená kontrola
        return redirect("/user/login")
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
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

def edit_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect('todo')
    else:
        form = TodoForm(instance=task)

    return render(request, 'todo/edit_task.html', {'form': form, 'task': task})
