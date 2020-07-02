from django.shortcuts import render,HttpResponse, redirect
from .models import Article,Section
from .forms import NewArticle
from django.contrib import messages
from django.contrib.auth.models import User 
from django.core.paginator import Paginator

def show_articles (request,section):
    section_id=Section.objects.get(name=section)
    display= Article.objects.filter(section_id=section_id.id)
   
    page = request.GET.get('page')
    paginator = Paginator(display, 2)
    page_paginator = paginator.get_page(page)

   


    return render (request,'articles/articles.html',{'display':display,
                                                    'title':section,"page_paginator":page_paginator
                                                  })

def new_articles (request):
   
    if request.method=="POST":
        user_id=request.user
        new_article= NewArticle(request.POST,request=request)
        new_article.user=user_id
        
        if new_article.is_valid():
           new_article.user=user_id
            
           new_article=new_article.save(commit=False)    
           new_article.user=request.user
           new_article.save()

           messages.success(request,"Tu articulo se a creado exitosamente !") 
           return redirect ("my_articles")    

        else:
            
            NewArticle_form=NewArticle(request=request)

            return render ( request,"articles/new_articles.html",{"NewArticle_form":NewArticle_form})

    else:
       
        NewArticle_form=NewArticle(request=request)

    return render ( request,"articles/new_articles.html",{"NewArticle_form":NewArticle_form})


def my_articles (request):

    user_id=request.user.id
    article=Article.objects.filter(user=user_id)
    page = request.GET.get('page')
    paginator = Paginator(article, 2)
    page_paginator = paginator.get_page(page)

    return render(request,"articles/my_articles.html",{"page_paginator":page_paginator})

def delete_article (request,title):

    article= Article.objects.get(title=title)
    article.delete()

    messages.success(request,"Tu articulo se a eliminado !") 
    return redirect ("my_articles")    
