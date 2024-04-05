# coding:utf-8
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Doctor(models.Model):
	name = models.CharField(verbose_name=u"医生名字", max_length=300)
	name_en = models.CharField(verbose_name=u"医生英文名", max_length=300)
	face = models.ImageField(upload_to="doctor/face", verbose_name=u"医生头像")
	college = models.CharField(verbose_name=u"毕业大学", max_length=300)
	ctime = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

	class Meta:
		verbose_name = u"医生"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name








@python_2_unicode_compatible
class Hospital(models.Model):
	name = models.CharField(verbose_name=u"医院名称", max_length=300)
	name_en = models.CharField(verbose_name=u"医院名称英文", max_length=300)
	logo = models.ImageField(upload_to="hospital/logo", verbose_name=u"医院logo")
	desc = models.CharField(max_length=500, verbose_name=u"医院简介")
	address = models.CharField(max_length=300, verbose_name=u"地点")
	project = models.CharField(verbose_name=u"项目",choices=(("ivf","IVF"),("egg","捐卵"),("sur","代孕"),("jj","捐精"),("fe","冻卵")), max_length=3)
	web = models.URLField(verbose_name=u"官方网站",max_length=100,default='')
	doctors = models.ManyToManyField(Doctor)
	ctime = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

	class Meta:
		verbose_name = u"医院"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name















