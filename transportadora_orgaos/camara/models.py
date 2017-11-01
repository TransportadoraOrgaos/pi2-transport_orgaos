from __future__ import unicode_literals
from django.db import models


class Camara(models.Model):
 name = models.CharField(max_length = 50, null=False)
