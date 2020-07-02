
from django.urls import path
from contacto import views

urlpatterns = [
   
    path("contacto",views.contacto,name="contacto") , 
]