# coding:utf-8
from django.contrib import admin
from .models import School
# Register your models here.


class SchoolAdmin(admin.ModelAdmin):
	list_display = ['name', 'ctime']
	search_display = ['name', 'ctime']
	list_filter = ['name', 'category', 'tag_leibie', 'provice', 'ctime']



admin.site.register(School, SchoolAdmin)