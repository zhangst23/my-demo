# coding:utf-8
from django.conf.urls import url 
from django.conf import settings
from .views import LanguageListView, LanguageDetailView

app_name = 'language'
urlpatterns = [
	url(r'^$', LanguageListView.as_view(), name='index'),
	url(r'^detail/(?P<language_id>\d+)/$', LanguageDetailView.as_view(), name='detail'),
]