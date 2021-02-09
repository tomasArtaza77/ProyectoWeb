from django.shortcuts import render, HttpResponse
from blog.models import Post, Categoria
# Create your views here.

def blog(request):
    posts = Post.objects.all() #importo todos los objetos que tengo en la clase Servicio
    return render(request,"blog/blog.html", {'posts': posts}) 

def categoria(request,categoria_id): 
    categoria = Categoria.objects.get(id = categoria_id) 
    posts = Post.objects.filter(categorias_post = categoria) 
    #{'categoria':categoria},{'posts': posts}
    return render(request,"blog/categoria.html",{'posts': posts,'categoria_param':categoria}) 