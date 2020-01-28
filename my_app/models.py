# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=255,verbose_name='Nome')
  description = models.TextField(null=True,blank=True,verbose_name='Descrição')

  class Meta:
    verbose_name = 'Categoria'
    verbose_name_plural = 'Categorias'

  def __str__(self):
    return self.name

class Post(models.Model):
  title = models.CharField(max_length=255,verbose_name='Título')
  subtitle = models.CharField(max_length=255,null=True,blank=True,verbose_name='Sub-título')
  content = models.TextField(verbose_name='Conteúdo')
  user = models.ForeignKey(User,on_delete=models.PROTECT,verbose_name='Autor')
  categories = models.ManyToManyField(Category,verbose_name='Categorias')

  class Meta:
    verbose_name = 'Artigo'
    verbose_name_plural = 'Artigos'

  def __str__(self):
    return self.title