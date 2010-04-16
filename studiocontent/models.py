#coding:utf-8
from django.db import models

# 网站内容，包括标题和内容
class SiteContent(models.Model):
	title=models.CharField(max_length=255)
	content=models.TextField()
	def __unicode__(self):
		return self.title
		
#某个网站内容的子类
class SubContent(models.Model):
	sitecontent=models.ForeignKey(SiteContent)
	title=models.CharField(max_length=255)
	content=models.TextField()
	def __unicode__(self):
		return self.title