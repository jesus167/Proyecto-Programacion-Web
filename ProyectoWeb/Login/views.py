from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login(request):
    return render(request, 'login/login.html')


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            messages.success(request, f"Bienvenido {username}")

            if user is not None:
                login(request, user)
                return redirect('ProyectoWebApp/index.html')
    return render(request, "login/login.html", {'form' : form})

def logout(request):
    logout(request)
    return redirect('/')