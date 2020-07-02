from django import forms
from django.core import validators
from contacto import models
class FormContacto (forms.ModelForm):
    
    class Meta:
        model= models.Contacto
        fields=("email","motive","content")
        labels= {"email":"Ingresa tu email","content":"Comentanos que sucede : "
                , "motive":" Seleccion el motivo por que cual quieres contactarnos :"}    




 