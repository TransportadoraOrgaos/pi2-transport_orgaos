from __future__ import unicode_literals
from django.db import models

# # Create your models here.


class Camara(models.Model):
 name = models.CharField(max_length = 50, null=False)
 responsible = models.CharField(max_length = 50, null=False)
 organ = models.CharField(max_length=50, null=False)


 def __unicode__(self):
 	return "{} - {}".format(self.id,self.name)


