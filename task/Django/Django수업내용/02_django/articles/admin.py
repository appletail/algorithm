from atexit import register
from django.contrib import admin
from articles.models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'content', 'created_at', 'updated_at']

admin.site.register(Article, ArticleAdmin)