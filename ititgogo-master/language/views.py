# coding:utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Language, Framework
from django.views.generic.base import View
# Create your views here.


class LanguageListView(View):
	def get(self, request):
		all_language = Language.objects.all().order_by('-ctime')

		return render(request, 'language/index.html',{
			'all_language': all_language,
		})




class LanguageDetailView(View):
	def get(self, request, language_id):
		language = Language.objects.get(id=int(language_id))
		

		return render(request, 'language/detail.html', {
			'language': language,
		})

