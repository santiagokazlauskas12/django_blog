from django.shortcuts import render, HttpResponse,redirect 
from . import forms 
from django.contrib import messages
from django.contrib.auth.decorators import  login_required
from django.contrib.auth import  authenticate,login,logout


def index (request):
    

    if request.method == "POST":

        
        username= request.POST.get("username")
        password= request.POST.get("password")
    
        user=authenticate(request,username=username,password=password)

        if user is not None: 
            login(request,user)
            return render (request,"mainapp/index.html",{"title":"home"})

        else:
            messages.error(request,"El usuario o la constraseña no son validos")
            return render (request,"mainapp/index.html",{"title":"home"})

    else:
                 
        return render(request,"mainapp/index.html",{"title":"home"})


def logout_user(request):
    logout(request)
    return redirect ("index")


def create_user (request):
    

    if request.method=="POST":
        create_user= forms.CreateUser(request.POST)
        if create_user.is_valid():
            create_user.save()
        

            messages.success(request,"Se a creado el usuario satisfactoriamente. Bienvenido !")
            return redirect("index")

        else:
            return render (request,"mainapp/new_user.html",{"create_user":create_user})
    else:
        create_user= forms.CreateUser()
   
        return render (request,"mainapp/new_user.html",{"create_user":create_user})

def nosotros (request):

    return render(request,"mainapp/nosotros.html")





 