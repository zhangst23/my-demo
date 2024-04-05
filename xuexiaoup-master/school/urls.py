# coding:utf-8
from django.conf.urls import url 
from . import views

app_name = 'school'
urlpatterns = [
	url(r'^$', views.SchoolListView.as_view(), name='index'),
	url(r'^school/(?P<school_id>[0-9]+)/$', views.SchoolDetailView.as_view(), name='detail'),
]