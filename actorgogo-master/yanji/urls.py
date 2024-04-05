# -*- coding: utf-8 -*-

from django.conf.urls.static import static
from django.conf.urls import url 
from django.conf import settings


from . import views

app_name = 'yanji'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^actor/$', views.ActorView.as_view(), name='actor_list'),
	url(r'^yanji/(?P<pk>[0-9]+)/$', views.YanjiDetailView.as_view(), name='detail'),
	url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
	url(r'^actor/ptitle/(?P<pk>[0-9]+)/$', views.ActorPtitleView.as_view(), name='act_ptitle_list'),
	url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
	url(r'^actor/(?P<pk>[0-9]+)/$', views.ActorDetailView.as_view(), name='actor'),
	url(r'^drama/$', views.DramaView.as_view(), name='drama_list'),
	url(r'^drama/(?P<pk>[0-9]+)/$', views.DramaDetailView.as_view(), name='drama'),
	url(r'^taici/$', views.TaiciView.as_view(), name='taici_list'),
	url(r'^taici/(?P<pk>[0-9]+)/$', views.TaiciDetailView.as_view(), name='taici'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



