# coding:utf-8
from django.conf.urls import url 
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'hospital'
urlpatterns = [
	url(r'^$', views.HospitalListView.as_view(), name='hospital_list'),
	url(r'^hospital/(?P<hospital_id>[0-9]+)/$', views.HospitalDetailView.as_view(), name='hospital_detail'),
	url(r'^doctorlist/$', views.DoctorListView.as_view(), name='doctor_list'),
	url(r'^doctor/(?P<doctor_id>\d+)/$', views.DoctorDetailView.as_view(), name='doctor_detail'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)