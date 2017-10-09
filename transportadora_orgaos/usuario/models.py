from __future__ import unicode_literals
from django.db import models

class Usuario(models.Model):
	username = models.CharField(max_length = 50, null=False)
 	password = models.CharField(max_length = 50, null=False)
 	email = models.CharField(max_length=50, null=False)
	
	def __unicode__(self):
 		return "{} - {}".format(self.id,self.name)