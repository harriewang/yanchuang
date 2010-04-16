#coding:utf-8
from django.db import models

class Case(models.Model):
	caseName=models.CharField(max_length=100)  #案例名称
	caseCaption=models.TextField()  #案例描述
	caseUrl=models.URLField()  #案例地址 
	caseImageUrl=models.URLField()  #案例截图地址
	caseThumbUrl=models.URLField()  #截图缩略图地址
	caseTime=models.CharField(max_length=20) #案例实际完成时间
	addTime=models.DateTimeField(auto_now_add=True)  #案例添加时间
	
	class Meta:
		ordering=['-addTime']
	
	def __unicode__(self):
		return self.caseName