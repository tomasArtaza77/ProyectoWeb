from django.shortcuts import render
from servicios.models import Servicio
# Create your views here.

def servicios(request):
    servicios = Servicio.objects.all() #importo todos los objetos que tengo en la clase Servicio
    return render(request,"servicios/servicios.html", {"servicios": servicios})