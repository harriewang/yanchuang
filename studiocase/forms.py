#coding:utf-8
from django import forms

class CaseForm(forms.Form):
	caseName=forms.CharField(label="案例名称")
	caseUrl=forms.CharField(label="案例地址")
	caseTime=forms.CharField(label="完成时间")
	caseImage=forms.ImageField(label="案例截图")
	caseCaption=forms.CharField(label="案例描述",widget=forms.Textarea)