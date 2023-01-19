from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroUserForm

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Bienvenido')
            return redirect('home')
        else:
            messages.success(request, 'Ha ocurrido un error, intenta de nuevo.')
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Sesión Cerrada.')
    return redirect('login')

def registrar(request):
    if request.method == 'POST':
        form = RegistroUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, 'Registro exitoso')
            return redirect('home')
    else:
        form = RegistroUserForm()
    return render(request, 'authenticate/registro.html', {'form':form})