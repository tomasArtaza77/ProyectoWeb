from . import views
from django.urls import path 


app_name = "carro" #me facilita la utilizacion de estas urls

urlpatterns = [
    
    path('agregar/<int:producto_id>/', views.agregar_producto, name="agregar"), 
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="eliminar"),
    path('restar/<int:producto_id>/', views.restar_producto, name="restar"), 
    path('limpiar/', views.limpiar_carro, name="limpiar"),  

]

