#coding:utf-8
from django.db import models

class Inquiry(models.Model):
	name=models.CharField(max_length=30)  #姓名
	tel=models.CharField(max_length=30)  #电话
	mobile=models.CharField(max_length=30)  #手机 
	email=models.EmailField() #E-mail
	budget=models.CharField(max_length=30) #预算
	requirement=models.TextField() #设计需求
	time=models.DateField(auto_now_add=True) #询价时间
	
	class Meta:
		ordering=['-time']
	
	def __unicode__(self):
		return self.name