# coding:utf-8
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View 
from django.http import HttpRequest, HttpResponse
from .models import School
# Create your views here.



class SchoolListView(View):
	def get(self, request):
		all_schools = School.objects.all()

		return render(request, 'school/index.html', {
			'all_schools':all_schools,

		})


class SchoolDetailView(View):
	def get(self, request, school_id):
		school = School.objects.get(id=int(school_id))

		return render(request, 'school/detail.html', {
			'school':school,
		})











