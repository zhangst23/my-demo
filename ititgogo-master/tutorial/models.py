# coding:utf-8
from __future__ import unicode_literals

import language

from django.db import models
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
# from language.models import Language
# Create your models here.


@python_2_unicode_compatible
class Tutorial(models.Model):
	title = models.CharField(verbose_name='教程名称', max_length=150)
	language = models.ForeignKey('language.Language')
	desc = models.TextField(verbose_name='简介')
	ctime = models.DateTimeField(verbose_name='添加时间', null=True)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('tutorial:detail', kwargs={'pk':self.pk})

	class Meta:
		verbose_name = '教程指南'
		verbose_name_plural = verbose_name



@python_2_unicode_compatible
class Tutorial_item(models.Model):
	name = models.CharField(verbose_name='教程章节', max_length=150)
	tutorial = models.ForeignKey(Tutorial)
	content = models.TextField(verbose_name='章节内容')
	ctime = models.DateTimeField(verbose_name='添加时间', null=True)


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('tutorial:item', kwargs={'pk':self.pk})

	class Meta:
		verbose_name = '教程章节'
		verbose_name_plural = verbose_name	














