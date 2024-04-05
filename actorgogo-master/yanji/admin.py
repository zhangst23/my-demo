# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Yanji, Category, Tag, Actor, Ptitle, Drama, Taici, Dramatype, Movietv, Movietype

class YanjiAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'ctime']

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name']

class TagAdmin(admin.ModelAdmin):
	list_display = ['name']

class ActorAdmin(admin.ModelAdmin):
	list_display = ['name', 'ptitle', 'ctime']

class PtitleAdmin(admin.ModelAdmin):
	list_display = ['name']

class DramaAdmin(admin.ModelAdmin):
	list_display = ['name', 'movietv', 'dramatype', 'ctime']

class TaiciAdmin(admin.ModelAdmin):
	list_display = ['title', 'movietv', 'ctime']

class DramatypeAdmin(admin.ModelAdmin):
	list_display = ['name', 'ctime']

class MovietvAdmin(admin.ModelAdmin):
	list_display = ['name', 'ctime', 'movietype']

class MovietypeAdmin(admin.ModelAdmin):
	list_display = ['name', 'ctime']






admin.site.register(Yanji, YanjiAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Ptitle, PtitleAdmin)
admin.site.register(Drama, DramaAdmin)
admin.site.register(Taici, TaiciAdmin)
admin.site.register(Dramatype, DramatypeAdmin)
admin.site.register(Movietv, MovietvAdmin)
admin.site.register(Movietype, MovietypeAdmin)










