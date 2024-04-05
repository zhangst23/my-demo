# coding:utf-8
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View 
from django.http import HttpResponse, HttpRequest
from .models import Hospital, Doctor

# Create your views here.
# 医院列表页
class HospitalListView(View):
	def get(self, request):
		all_hospital = Hospital.objects.all().order_by('-ctime')

		return render(request, 'hospital/hospital_list.html', {
			'all_hospital':all_hospital,
		})


class HospitalDetailView(View):
	def get(self, request, hospital_id):
		hospital = Hospital.objects.get(id=int(hospital_id))

		return render(request, 'hospital/hospital_detail.html', {
			'hospital':hospital,
			})


class DoctorListView(View):
	def get(self, request):
		all_doctor = Doctor.objects.all().order_by('-ctime')

		return render(request, 'hospital/doctor_list.html', {
			'all_doctor':all_doctor,
			})


class DoctorDetailView(View):
	def get(self, request, doctor_id):
		doctor = Doctor.objects.get(id=int(doctor_id))

		return render(request, 'hospital/doctor_detail.html', {
			'doctor':doctor,
			})












