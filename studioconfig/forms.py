#coding:utf-8
from django import forms 

class ConfigForms(forms.Form):
	title=forms.CharField(label='网站名称',max_length=255,required=True)
	description=forms.CharField(label='网站描述',max_length=255,required=True)
	keywords=forms.CharField(label='网站关键词',max_length=255,required=True)