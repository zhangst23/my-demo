# coding:utf-8
from django.conf.urls import url 
from .views import TutorialListView, TutorialDetailView

app_name = 'tutorial'
urlpatterns = [
	url(r'^$', TutorialListView.as_view(), name='index'),
	url(r'^tutorial/(?P<tutorial_id>\d+)/$', TutorialDetailView.as_view(), name='detail'),
]