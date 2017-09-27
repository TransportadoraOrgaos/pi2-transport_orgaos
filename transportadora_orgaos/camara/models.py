from __future__ import unicode_literals
from django.db import models

# # Create your models here.


class Camara(models.Model):
 name = models.CharField(max_length = 50)


 def __unicode__(self):
 	return "{} - {}".format(self.id,self.name)


