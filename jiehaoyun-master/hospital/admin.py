# coding:utf-8
from django.contrib import admin
from .models import Hospital, Doctor
# Register your models here.

class HospitalAdmin(admin.ModelAdmin):
	list_display = ['name', 'name_en', 'web']
	search_fileds = ['name', 'name_en']
	list_filter = ['project']


class DoctorAdmin(admin.ModelAdmin):
	list_display = ['name', 'name_en']
	search_fileds = ['name', 'name_en']
	list_filter = ['hospital']


admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Doctor, DoctorAdmin)