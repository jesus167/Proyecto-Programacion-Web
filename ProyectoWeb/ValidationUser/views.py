from django.shortcuts import redirect, render
from .forms import CreateUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.


def registro(request):

    data = {'form': CreateUserForm}
    # Validar metodo Post
    if request.method == 'POST':
        formulario = CreateUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            # Autenticar Usuario
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username = username, password= password)
            login(request, user)
            return redirect(to='Home')
        else:
            messages.success(request, "Hubo un error")
            print("hubo un error")

    return render(request, 'registro/register.html', data)