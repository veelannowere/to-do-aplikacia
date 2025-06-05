from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login as auth_login

from .forms import TodoForm
from .models import Todo

def index(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

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
    todo = get_object_or_404(Todo, id=item_id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/edit.html', {'form': form, 'todo': todo})
