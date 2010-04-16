#coding:utf-8
from django.db import models

#网站动态
class News(models.Model):
	title=models.CharField(max_length=255)  #动态标题
	type=models.CharField(max_length=20) #动态类型：分为“新闻”，“进行中”，“已完成”
	content=models.TextField()  #动态内容
	time=models.DateTimeField(auto_now_add=True) #动态添加时间
	
	class Meta:
		ordering=['-time']
		
	def __unicode__(self):
		return self.title