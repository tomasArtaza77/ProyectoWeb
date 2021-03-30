from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage
# Create your views here.


def contacto(request): 
    formulario_contacto = FormularioContacto()

    if request.method=="POST": #rescato info de los cuadros de txt
        formulario_contacto = FormularioContacto(data=request.POST)

        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            asunto = request.POST.get("asunto") 

            email = EmailMessage("Mensaje desde App Django",
            "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre,email,asunto),
            "",["tomasartaza25@gmail.com"],reply_to=[email]) 

            try: 
                email.send()  
                return redirect("/contacto/?valido") # el ? verifica info. para el GET
            
            except:
                return redirect("/contacto/?no-valido") # el ? verifica info. para el GET

    return render(request,"contacto/contacto.html", {"formulario":formulario_contacto}) 