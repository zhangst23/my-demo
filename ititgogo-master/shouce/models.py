# coding:utf-8
from __future__ import unicode_literals

import language


from django.db import models
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
# Create your models here.


@python_2_unicode_compatible
class Shouce(models.Model):
	name = models.CharField(verbose_name='手册名称', max_length=150)
	url = models.URLField(max_length=300, verbose_name='链接')
	language = models.ForeignKey('language.Language')
	desc = models.TextField(verbose_name='简介')
	ctime = models.DateTimeField(verbose_name='添加时间', null=True)

	def __str__(self):
		return self.name

	# def get_absolute_url(self):
	# 	return reverse('shouce:detail', kwargs={'pk':self.pk})

	class Meta:
		verbose_name = '手册'
		verbose_name_plural = verbose_name













