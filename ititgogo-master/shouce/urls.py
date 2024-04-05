# coding:utf-8
from django.conf.urls import url 
from django.conf import settings
from .views import ShouceListView

app_name = 'shouce'
urlpatterns = [
	url(r'^$', ShouceListView.as_view(), name='index'),
]