# coding:utf-8
from django.contrib import admin
from .models import Shouce
# Register your models here.


class ShouceAdmin(admin.ModelAdmin):
	list_display = ['name', 'language', 'ctime']
	search_fields = ['name']
	list_filter = ['name']



admin.site.register(Shouce, ShouceAdmin)