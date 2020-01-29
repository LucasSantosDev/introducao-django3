# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
  return HttpResponse('Olá Mundo')

def home_param(request, post_id):
  return HttpResponse('Olá Mundo!!! %s' % post_id)

def posts_index(request):
  posts = Post.objects.all()
  return render(request, 'posts/index.html', {
    'posts': posts
  })

def posts_show(request, post_id):
  post = Post.objects.get(id=post_id)
  return render(request, 'posts/show.html', {
    'post': post
  })