from django.shortcuts import redirect, render
from .forms import FormularioContacto
# Create your views here.


def contacto(request): 
    formulario_contacto = FormularioContacto()

    if request.method=="POST": #rescato info de los cuadros de txt
        formulario_contacto = FormularioContacto(data=request.POST)

        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            asunto = request.POST.get("asunto") 

            return redirect("/contacto/?valido") # el ? verifica info. para el GET

    return render(request,"contacto/contacto.html", {"formulario":formulario_contacto}) 