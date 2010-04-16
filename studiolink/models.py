#coding:utf-8
from django.db import models

class Link(models.Model):
	linkTitle=models.CharField(max_length=100)  #友情链接名称
	linkUrl=models.URLField() #友情链接地址
	
	def __unicode__(self):
		return self.linkTitle