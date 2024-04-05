# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

import django.utils.timezone as timezone



@python_2_unicode_compatible
class Category(models.Model):
	name = models.CharField(verbose_name='演技分类', max_length=100)

	def __str__(self):
		return self.name

	# def get_absolute_url(self):
	# 	return reverse('yanji:cate_list', kwargs={'pk':self.pk})

	class Meta():
		verbose_name = '演技分类'
		verbose_name_plural = verbose_name




@python_2_unicode_compatible
class Tag(models.Model):
	name = models.CharField(verbose_name='演技标签', max_length=100)


	def __str__(self):
		return self.name

	class Meta():
		verbose_name = '演技标签'
		verbose_name_plural = verbose_name




@python_2_unicode_compatible
class Ptitle(models.Model):
	name = models.CharField('演员职称', max_length=100, blank=True)
	ctime = models.DateTimeField(verbose_name='添加时间', null=True, default=timezone.now)

	def __str__(self):
		return self.name

	class Meta():
		verbose_name = '演员职称'
		verbose_name_plural = verbose_name



@python_2_unicode_compatible
class Actor(models.Model):
	name = models.CharField(verbose_name='演员', max_length=100)
	touxiang = models.FileField(verbose_name='头像', upload_to='yanyuan_tx/', null=True, blank=True)
	ctime = models.DateTimeField(verbose_name='添加时间', null=True, default=timezone.now)
	ptitle = models.ForeignKey(Ptitle, blank=True)


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('yanji:act_detail', kwargs={'pk':self.pk})


	class Meta():
		verbose_name = '演员'
		verbose_name_plural = verbose_name

@python_2_unicode_compatible
class Movietype(models.Model):
	name = models.CharField(verbose_name='影视剧类型', max_length=100)
	ctime = models.DateTimeField(verbose_name='添加时间', null=True, default=timezone.now)

	def __str__(self):
		return self.name

	class Meta():
		verbose_name = '影视剧类型'
		verbose_name_plural = verbose_name	


@python_2_unicode_compatible
class Movietv(models.Model):
	movietype = models.ForeignKey(Movietype, blank=True, verbose_name='影视剧类型')
	name = models.CharField(verbose_name='影视剧名称', max_length=100)
	ctime = models.DateTimeField(verbose_name='添加时间', null=True, default=timezone.now)


	def __str__(self):
		return self.name

	class Meta():
		verbose_name = '影视剧'
		verbose_name_plural = verbose_name	



@python_2_unicode_compatible
class Dramatype(models.Model):
	name = models.CharField(verbose_name='剧本类型', max_length=100)
	ctime = models.DateTimeField(verbose_name='添加时间', null=True, default=timezone.now)

	def __str__(self):
		return self.name

	class Meta():
		verbose_name = '剧本类型'
		verbose_name_plural = verbose_name


@python_2_unicode_compatible
class Taici(models.Model):
	title = models.CharField(verbose_name='台词', max_length=100)
	movietv = models.ForeignKey(Movietv, verbose_name='影视剧')
	content = models.TextField(verbose_name='台词内容')
	ctime = models.DateTimeField(verbose_name='添加时间', null=True, default=timezone.now)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('yanji:taici_detail', kwargs={'pk':self.pk})

	class Meta():
		verbose_name = '台词'
		verbose_name_plural = verbose_name


@python_2_unicode_compatible
class Drama(models.Model):
	name = models.CharField(verbose_name='剧本', max_length=100)
	movietv = models.ForeignKey(Movietv, blank=True, verbose_name='影视剧', null=True)
	dramatype = models.ForeignKey(Dramatype, verbose_name='剧本类型')
	content = models.TextField(verbose_name='剧本内容')
	taici = models.ForeignKey(Taici, blank=True, verbose_name='台词', null=True)
	ctime = models.DateTimeField(verbose_name='添加时间', null=True, default=timezone.now)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('yanji:drama_detail', kwargs={'pk':self.pk})


	class Meta():
		verbose_name = '剧本'
		verbose_name_plural = verbose_name


@python_2_unicode_compatible
class Yanji(models.Model):
	STATUS_CHOICES = (
		('d', '草稿'),
		('p', '发表'),
	)
	status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES, default='p')
	actor = models.ManyToManyField(Actor, blank=True)
	title = models.CharField(verbose_name='标题', max_length=100)
	content = models.TextField(verbose_name='内容')
	category = models.ForeignKey(Category)
	tag = models.ManyToManyField(Tag, blank=True)
	movietv = models.ForeignKey(Movietv)
	fengmian = models.ImageField(verbose_name='封面图', upload_to='yanji_fengmian/', null=True, blank=True)
	video = models.URLField(verbose_name='视频地址', max_length=200, default='www.actorgogo.com')
	ctime = models.DateTimeField(verbose_name='添加时间', null=True, default=timezone.now)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('yanji:detail', kwargs={'pk':self.pk})


	class Meta():
		verbose_name = '演技'
		verbose_name_plural = verbose_name













