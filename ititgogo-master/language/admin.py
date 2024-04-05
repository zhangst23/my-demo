# coding:utf-8
from django.contrib import admin
from .models import Language, Framework
# Register your models here.

class LanguageAdmin(admin.ModelAdmin):
	list_display = ['name']
	list_filter = ['ctime']


class FrameworkAdmin(admin.ModelAdmin):
	list_display = ['name', 'language', 'ctime']
	search_fields = ['name']
	list_filter = ['name']


admin.site.register(Language, LanguageAdmin)
admin.site.register(Framework, FrameworkAdmin)