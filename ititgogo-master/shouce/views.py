# coding:utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Shouce
from django.views.generic.base import View
# Create your views here.


class ShouceListView(View):
	def get(self, request):
		all_shouce = Shouce.objects.all().order_by('-ctime')

		return render(request, 'shouce/index.html',{
			'all_shouce': all_shouce,
		})


