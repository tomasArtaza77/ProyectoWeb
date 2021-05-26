from django.urls import path
from . import views #llamo a views para trabajar con las urls

urlpatterns = [
    path('', views.blog, name="Blog"),   
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),   
                    
]