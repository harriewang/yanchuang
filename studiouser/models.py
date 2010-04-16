from django.db import models

# Create your models here.
class User(models.Model):
	email=models.EmailField(unique=True)
	username=models.CharField(max_length=255,unique=True)
	password=models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.email