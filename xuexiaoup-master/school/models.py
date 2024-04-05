# coding:utf-8
from __future__ import unicode_literals
from datetime import datetime 
from django.db import models
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
# Create your models here.



@python_2_unicode_compatible
class School(models.Model):
	name = models.CharField(verbose_name='学校名称', max_length=100)
	desc = models.TextField(verbose_name='学校简介')
	logo = models.ImageField(upload_to='school_logo', null=True, blank=True)
	category = models.CharField(choices=(('dx','大学'),('zx','中学'),('gz','高中'),('cz','初中'),('xx','小学'),('yey','幼儿园')), max_length=3, verbose_name='学校级别')
	tag_leibie = models.CharField(default='211高校', verbose_name='学校类别', max_length=50)
	name_en = models.CharField(verbose_name='英文名称', max_length=100)
	alias = models.CharField(verbose_name='简称', max_length=100)
	provice = models.CharField(verbose_name='地区', max_length=100)
	begintime = models.CharField(verbose_name='成立时间', max_length=50)
	guanwang = models.CharField(verbose_name='官网', max_length=100)
	position = models.CharField(verbose_name='地址', max_length=300)
	xiaoxun = models.CharField(verbose_name='校训', max_length=300)
	yuanxi = models.TextField(verbose_name='主要院系')
	story = models.TextField(verbose_name='学校历史')
	xueshu = models.TextField(verbose_name='学术资源')
	zhuanye = models.TextField(verbose_name='学校专业')
	zhaosheng = models.TextField(verbose_name='招生就业')
	ctime = models.DateTimeField(default=datetime.now, verbose_name='添加时间')


	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '学校'
		verbose_name_plural = verbose_name

























