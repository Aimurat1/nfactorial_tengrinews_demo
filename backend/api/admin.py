from django.contrib import admin

# Register your models here.
from .models import NewsInstance, NewsTag

class NewsInstanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'datetime']

admin.site.register(NewsInstance, NewsInstanceAdmin)
admin.site.register(NewsTag)
