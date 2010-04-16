from django.db import models

# Create your models here.
class StudioConfig(models.Model):
	title=models.CharField(max_length=255)
	description=models.CharField(max_length=255)
	keywords=models.CharField(max_length=255)