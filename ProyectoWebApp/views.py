from django.shortcuts import render 

# Create your views here.

#Creo tantas vistas como páginas y urls que vaya a tener.

def inicio(request):
    return render(request,"ProyectoWebApp/inicio.html")     
 
