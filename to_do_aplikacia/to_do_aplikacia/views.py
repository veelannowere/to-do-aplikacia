from django.shortcuts import render, redirect
from django.contrib import messages



def home(request):
    return redirect('todo')  # Redirect to the 'todo' view
       # return render(request,'todo/index.html')
