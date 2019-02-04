# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Item (models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    color = models.CharField(max_length=255, null = True)
    img = models.CharField(max_length=255, null = True)
    review = models.TextField(null= True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)