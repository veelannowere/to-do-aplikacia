from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, RegisterForm


def sign_in(request):
    print("sign_in called with method:", request.method)  # Debug print
    if request.method == 'GET':
        if request.user.is_authenticated:
            print("User is already authenticated")  # Debug print
            return redirect('todo')  # Changed from 'ulohy' to 'todo'
        
        form = LoginForm()
        return render(request,'users/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)
        print("Login form data:", form.data)  # Debug print
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password=form.cleaned_data['password']
            print("Form is valid. Username:", username)  # Debug print
            user = authenticate(request,username=username,password=password)
            if user:
                print("User authenticated successfully")  # Debug print
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('todo')  # Redirect to todo page after login
        
        # either form not valid or user is not authenticated
        print("Invalid login attempt")  # Debug print
        messages.error(request,f'Invalid username or password')
        return render(request,'users/login.html',{'form': form})


def sign_out(request):
    logout(request)
    request.session['logout_message'] = 'You have been logged out.'  # Store message in session
    return redirect('login')      

def sign_up(request):
    print("sign_up called with method:", request.method)  # Debug print
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        print("Register form data:", form.data)  # Debug print
        if form.is_valid():
            print("Form is valid")  # Debug print
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('login')  # Redirect to login page after registration
        else:
            print("Form is invalid")  # Debug print
            return render(request, 'users/register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print("Register form data:", form.data)
        if form.is_valid():
            form.save()
            # Automatically log in the user after registration
            print("Form is valid, user created")
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
