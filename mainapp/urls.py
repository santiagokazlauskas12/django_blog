from django.urls import path, include
from mainapp import views 
from django.contrib.auth import views as auth_views



urlpatterns = [
     path('', views.index,name="index"), 
     path('new_user', views.create_user,name="new_user"), 
     path('logout', views.logout_user,name="logout"),
     path('nosotros', views.nosotros,name="nosotros"),
     
     
     
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="mainapp/recover_pass/reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="mainapp/recover_pass/reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="mainapp/recover_pass/reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="mainapp/recover_pass/reset_succes.html"), 
        name="password_reset_complete"),

]