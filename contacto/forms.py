from typing import Text
from django import forms
from django.forms.fields import EmailField
#Comentario
class FormularioContacto(forms.Form):

    nombre = forms.CharField(label="Nombre",required=True)
    email = forms.EmailField(label="Email",required=True)
    asunto = forms.CharField(label="Asunto", widget=forms.Textarea,max_length=100) 

    