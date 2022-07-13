from django.shortcuts import render, redirect
from .forms import formulario_contacto
from django.core.mail import EmailMessage
# Create your views here.


def contacto(request):

    formulario = formulario_contacto()

    if request.method=="POST":

        formulariocontacto=formulario_contacto(data=request.POST)

        if formulariocontacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage("Mensaje desde App Django",
            "El usuario {} con el email {} escribre lo siguiente:\n\n {}".format(nombre,email,contenido),
            "", ["ogutierrespinosa@gmail.com"], reply_to=[email])

            try: 
                email.send()
                
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")
        
    return render(request, 'contacto/contacto.html', {'miFormulario': formulario})