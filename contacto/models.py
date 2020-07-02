from django.db import models
from django.db import models
from ckeditor.fields  import RichTextField 

class Contacto (models.Model):
     motive_fields=( ("sugerencia","Sugerencia"),
                     ("reclamo","Reclamo"),
                     ("otros","Otros..") )

     email=models.EmailField( max_length=254,verbose_name="Enviado por:")
     motive= models.CharField(choices=motive_fields , default="sugerencia",max_length=30)
     content=RichTextField(verbose_name="contenido")
     date = models.DateField(auto_now=True, verbose_name="Fecha de envio")

