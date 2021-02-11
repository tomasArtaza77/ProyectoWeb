from django.urls import path
from . import views #llamo a views para trabajar con las urls

urlpatterns = [

    path('', views.contacto, name="Contacto"),  

]
