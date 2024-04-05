# -*- coding: utf-8 -*-

from django import template
from ..models import Yanji, Category, Tag, Actor, Ptitle, Drama, Taici, Dramatype

register = template.Library()


@register.simple_tag
def get_categories():
	return Category.objects.all()


@register.simple_tag
def get_tags():
	return Tag.objects.all()


@register.simple_tag
def get_actors():
	return Actor.objects.all()


@register.simple_tag
def get_ptitles():
	return Ptitle.objects.all()

@register.simple_tag
def get_dramatypes():
	return Dramatype.objects.all()

@register.simple_tag
def get_dramas():
	return Drama.objects.all()


@register.simple_tag
def get_taicis():
	return Taici.objects.all()





	


















