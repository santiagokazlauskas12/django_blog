from django import forms
from django.core import validators
from articles import models 
from django.contrib.auth.models import User 


class NewArticle (forms.ModelForm):
  
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields["user"].queryset = User.objects.filter(id=self.request.user.id)
        

    class Meta:       
        model=models.Article
        fields=["title","article","section","user"]

        label= {"title":"Titulo", "article": "Articulo","section":"Seccion:"}


