from django.contrib import admin
from .models import Servicio


# Register your models here.

class Servicio_admin(admin.ModelAdmin):
    readonly_fields = ('updated','created') 

    


admin.site.register(Servicio, Servicio_admin) #agrego panel servicio 

