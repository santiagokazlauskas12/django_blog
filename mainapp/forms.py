from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class CreateUser (UserCreationForm):
    email=forms.EmailField(required=True)
  
  

    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]

