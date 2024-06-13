from django.contrib import admin
from .models import *

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Kitob, ArticleAdmin)
admin.site.register(Category, ArticleAdmin)
admin.site.register(BookDownloads)
