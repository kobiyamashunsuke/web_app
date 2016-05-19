from django.db import models
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your models here.


class Book(models.Model):
    """書籍"""
    func_name = models.CharField('関数名', max_length=255)
    program_name = models.CharField('プログラム名', max_length=255)
    tag = models.CharField('タグ名', max_length=255, blank=True)
    author = models.CharField('著者名', max_length=255, blank=True)
    Github = models.CharField('Github', max_length=255, blank=True)

class python_Book(models.Model):
    """書籍"""
    func_name = models.CharField('関数名', max_length=255)
    program_name = models.CharField('プログラム名', max_length=255)
    tag = models.CharField('タグ名', max_length=255, blank=True)
    author = models.CharField('著者名', max_length=255, blank=True)
    Github = models.CharField('Github', max_length=255, blank=True)

class Impression(models.Model):
    """感想"""
    book = models.ForeignKey(Book, verbose_name='関数名', related_name='impressions')
    comment = models.TextField('コメント', blank=True)

class python_Impression(models.Model):
    """感想"""
    book = models.ForeignKey(python_Book, verbose_name='関数名', related_name='impressions')
    comment = models.TextField('コメント', blank=True)

