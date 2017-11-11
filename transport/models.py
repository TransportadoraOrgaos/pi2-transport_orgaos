# -*-encoding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django import forms

# Create your models here.
class Transport(models.Model):   
    responsible = models.CharField(max_length = 50, null = False)
