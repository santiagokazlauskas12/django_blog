from django.contrib import admin
from articles import models


class ArticleAdmin(admin.ModelAdmin):     
    readonly_fields=('created_at',)
    
    def save_model (self,request,obj,form,change):
        if not obj.user_id:
            obj.user_id=request.user.id
        obj.save()    


admin.site.register(models.Section)
admin.site.register(models.Article,ArticleAdmin)



 
