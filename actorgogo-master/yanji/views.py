# -*- coding: utf-8 -*-
import markdown

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Yanji, Category, Tag, Actor, Ptitle, Drama, Taici, Dramatype
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator



class IndexView(ListView):
	model = Yanji
	template_name = 'yanji/index.html'
	context_object_name = 'yanji_list'
	paginate_by = 6




class YanjiDetailView(DetailView):
	model = Yanji
	template_name = 'yanji/detail.html'
	context_object_name = 'yanji'

	# def get(self, request, *args, **kwargs):
	# 	response = super(YanjiDetailView, self).get(request, *args, **kwargs)
	# 	return response

	# def get_object(self, queryset=None):
	# 	yanji = super(YanjiDetailView, self).get_object(queryset=None)
	# 	return yanji

    # def get_context_data(self, **kwargs):
    #     # 覆写 get_context_data 的目的是因为除了将 post 传递给模板外（DetailView 已经帮我们完成），
    #     # 还要把评论表单、post 下的评论列表传递给模板。
    #     context = super(YanjiDetailView, self).get_context_data(**kwargs)
    #     form = CommentForm()
    #     comment_list = self.object.comment_set.all()
    #     context.update({
    #         'form': form,
    #         'comment_list': comment_list
    #     })
    #     return context


class CategoryView(ListView):
	model = Yanji
	template_name = 'yanji/cate_list.html'
	context_object_name = 'yanji_list'

	def get_queryset(self):
		cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
		return super(CategoryView, self).get_queryset().filter(category=cate)


class TagView(ListView):
	model = Yanji
	template_name = 'yanji/tag_list.html'
	context_object_name = 'yanji_list'

	def get_queryset(self):
		tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
		return super(TagView, self).get_queryset().filter(tag=tag)




class ActorView(ListView):
	model = Yanji
	template_name = 'yanji/actor_list.html'
	context_object_name = 'actor_list'
	
	# def get_queryset(self):
	# 	Actor = get_object_or_404(Actor, pk=self.kwargs.get('pk'))
	# 	return super(ActorView, self).get_queryset().filter(actor=actor)


class ActorDetailView(DetailView):
	model = Actor
	template_name = 'yanji/actor_detail.html'
	context_object_name = 'actor'



class ActorPtitleView(ListView):
	model = Actor
	template_name = 'yanji/act_ptitle_list.html'
	context_object_name = 'actor_list'

	def get_queryset(self):
		ptitle = get_object_or_404(Ptitle, pk=self.kwargs.get('pk'))
		return super(PtitleView, self).get_queryset().filter(ptitle=ptitle)



class DramaView(ListView):
	model = Drama
	template_name = 'yanji/drama_list.html'
	context_object_name = 'drama_list'
	paginate_by = 10


class DramaDetailView(DetailView):
	model = Drama
	template_name = 'yanji/drama_detail.html'
	context_object_name = 'drama'


class TaiciView(ListView):
	model = Taici
	template_name = 'yanji/taici_list.html'
	context_object_name = 'taici_list'
	paginate_by = 10


class TaiciDetailView(DetailView):
	model = Taici
	template_name = 'yanji/taici_detail.html'
	context_object_name = 'taici'















