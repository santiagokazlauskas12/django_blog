from django.db import models
from django.contrib.auth.models import User 
from ckeditor.fields  import RichTextField 


class Section (models.Model):
    name= models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Article (models.Model):
    title= models.CharField(max_length=20,unique=True)
    article = RichTextField(verbose_name=" Articulo : ")   
    user = models.ForeignKey(User,verbose_name=" Usuario ",on_delete=models.CASCADE,null=True,blank=True) 
    section =models.ForeignKey(Section,on_delete=models.CASCADE)
    created_at = models.DateField(verbose_name="Creado el : " ,auto_now_add=True)    

    def __str__(self):
        return self.title



