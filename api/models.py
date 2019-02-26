# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.utils.translation import ugettext_lazy as _



class Category(models.Model):
    """
    A (sub) category can belong to another category 
    """
    main_category = models.ForeignKey('Category', verbose_name=_('Top Category'), related_name="subcategories", related_query_name="subcategory", null=True, blank=True)
    slug = models.SlugField(max_length=200, verbose_name=_('Slug'), null=True, blank=True)
    name = models.CharField(max_length=200, verbose_name=_('Name'), null=True, blank=True)
    enabled = models.BooleanField(verbose_name=_('Enabled'), default=True)
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
    def __str__(self):
        return "Category %s" % self.name


class Video(models.Model):
    """
    Video will contain a file to play and the votes
    """
    category = models.ForeignKey(Category, verbose_name=_('Category'), related_name="videos", related_query_name="video")
    
    name = models.CharField(max_length=200, null=True, blank=True)
    video = models.FileField(upload_to='videos/')
    thumbs_up = models.PositiveIntegerField(verbose_name=_('Thumbs Up'), default=0, blank=True)
    thumbs_down = models.PositiveIntegerField(verbose_name=_('Thumbs Down'), default=0, blank=True)
    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')
    def __str__(self):
        return self.name
