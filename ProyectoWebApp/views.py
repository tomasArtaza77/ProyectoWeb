from django.shortcuts import render 

# Create your views here.

#Creo tantas vistas como páginas y urls que vaya a tener.

def inicio(request):
    return render(request,"ProyectoWebApp/inicio.html")     

def tienda(request):
    return render(request,"ProyectoWebApp/tienda.html")  

def contacto(request): 
    return render(request,"ProyectoWebApp/contacto.html")   
