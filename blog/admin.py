from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','pub_time')
    list_filter = ('pub_time',)

# 注册后台管理系统
admin.site.register(Article, ArticleAdmin)

