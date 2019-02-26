# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from api import models



admin.site.register(models.Category)

admin.site.register(models.Video)

