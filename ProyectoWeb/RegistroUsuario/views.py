from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import View


# Create your views here.


<<<<<<< HEAD

def registro( request):
    form = UserCreationForm()
    return render(request, 'registro/register.html', {'form': form})

def registro_final(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        usuario = form.save()
        nombre_usuario = form.cleaned_data.get("username")
        messages.success(request, f"Bienvenid@ a La casa de las Flores: {nombre_usuario}")
        login(request, usuario)
        return redirect("Home")
    else:
        messages.error(request, "Error al registrar usuario")
    
=======
def registro(request):


    return render(request, "registro/registro.html")
>>>>>>> 128f23bed87f8a9a4e0bea8c474957b0d83c30c8
