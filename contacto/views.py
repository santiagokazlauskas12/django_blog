from django.shortcuts import render,HttpResponse
from contacto import forms
from django.contrib import messages
from  django.core.mail import send_mail

def contacto (request):

    if request.method == "POST":
        save_mail=forms.FormContacto(request.POST)    
        if save_mail.is_valid():
            save_mail.save()
            form=forms.FormContacto()

            subject=request.POST["motive"]
            mail=request.POST["email"]

            content="Muchas gracias por ponerte en contacto con nosotro a la brevedad estaremos respondiendo"
            

            send_mail(subject,content,"djangosantiagodjango@gmail.com",(mail,))



            
            messages.success(request,"Tu mensaje se ah enviado correctamente")
            return render(request,"contacto/contacto.html",{"form":form,"title":"Contacto"})
        else:
            form=forms.FormContacto()    
            return render(request,"contacto/contacto.html",{"form":form,"title":"Contacto"})
    else:

        form=forms.FormContacto()

        return render(request,"contacto/contacto.html",{"form":form,"title":"Contacto"})