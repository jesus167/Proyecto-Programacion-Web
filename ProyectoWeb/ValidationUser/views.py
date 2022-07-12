from django.shortcuts import redirect, render
from .forms import CreateUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.


def registro(request):

    data = {'form': CreateUserForm}
    # Validar metodo Post
    if request.method == 'POST':
        formulario = CreateUserForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            # Autenticar Usuario
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username = username, password= password)
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to='Home')
        else:
            messages.success(request, "Debe llenar todos los campos solicitados")
        data['form'] = formulario
    return render(request, 'registro/register.html', data)