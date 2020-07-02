from django.urls import path
from articles import views 




urlpatterns = [ 
    path('articles/<str:section>', views.show_articles,name="articles"), 
    path('new_articles', views.new_articles,name="new_articles"), 
    path('my_articles', views.my_articles,name="my_articles"), 
    path('delete_article/<str:title>', views.delete_article,name="delete_article"),
]
     