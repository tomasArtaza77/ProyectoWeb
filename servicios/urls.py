from django.urls import path
from . import views #llamo a views para trabajar con las urls

urlpatterns = [ 
    path('', views.servicios, name="Servicios"), 
]
