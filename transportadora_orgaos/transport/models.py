from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Transport(models.Model):
    organ = models.CharField(max_length = 50, null = False)
    responsible = models.CharField(max_length = 50, null = False)
