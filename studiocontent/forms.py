#coding:utf-8
from django import forms

class AddContentForm(forms.Form):
	title=forms.CharField(max_length=255,required=True)
	parent=forms.CharField(max_length=100)
	content=forms.CharField(widget=forms.Textarea)
	
