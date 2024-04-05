# coding:utf-8
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
# Create your models here.



@python_2_unicode_compatible
class Language(models.Model):
	name = models.CharField(verbose_name='编程语言', max_length=100)
	ctime = models.DateTimeField(default=datetime.now, verbose_name='添加时间', null=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('language:detail', kwargs={'pk':self.pk})

	class Meta:
		verbose_name = '编程语言'
		verbose_name_plural = verbose_name



@python_2_unicode_compatible
class Framework(models.Model):
	name = models.CharField(verbose_name='框架', max_length=100)
	language = models.ForeignKey(Language)
	ctime = models.DateTimeField(default=datetime.now, verbose_name='添加时间', null=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '框架'
		verbose_name_plural = verbose_name




