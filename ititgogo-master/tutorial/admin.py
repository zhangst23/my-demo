# coding:utf-8
from django.contrib import admin
from .models import Tutorial, Tutorial_item
# Register your models here.


class TutorialAdmin(admin.ModelAdmin):
	list_display = ['title', 'language', 'ctime']
	search_fields = ['title']
	list_filter = ['title']


class Tutorial_itemAdmin(admin.ModelAdmin):
	list_display = ['name', 'tutorial', 'ctime']
	search_fields = ['name']
	list_filter = ['name']

admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Tutorial_item, Tutorial_itemAdmin)





