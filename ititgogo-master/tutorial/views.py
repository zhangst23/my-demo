# coding:utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Tutorial, Tutorial_item
from django.views.generic.base import View
# Create your views here.


class TutorialListView(View):
	def get(self, request):
		all_tutorials = Tutorial.objects.all().order_by('-ctime')

		return render(request, 'tutorial/index.html',{
			'all_tutorials':all_tutorials,
		})




class TutorialDetailView(View):
	def get(self, request, tutorial_id):
		tutorial = Tutorial.objects.get(id=int(tutorial_id))
		tutorial_item = Tutorial_item.objects.get(id=int(tutorial_id))
		

		return render(request, 'tutorial/detail.html', {
			'tutorial': tutorial,
			'tutorial_item':tutorial,
		})

