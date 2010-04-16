#coding:utf-8
from django import forms

class LinkForm(forms.Form):
	linkTitle=forms.CharField(label="链接名称",required=True)
	linkUrl=forms.CharField(label="链接地址",required=True)