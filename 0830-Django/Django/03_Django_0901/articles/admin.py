from django.contrib import admin
from .models import Article # 현재 폴더에 있는 models 에 있는 Article 클래스를 가져와서

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'updated_at', )


# Register your models here.
admin.site.register(Article, ArticleAdmin) # 