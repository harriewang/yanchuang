#coding:utf-8
from django import forms

Type_Choice = (
	("新闻","新闻"),
	("进行中","进行中"),
	("已完成","已完成")
)

class AddNewsForm(forms.Form):
	title=forms.CharField(label="动态标题",max_length=255,required=True)
	type=forms.ChoiceField(label="动态类型",choices=Type_Choice,required=True)
	content=forms.CharField(label="动态内容",widget=forms.Textarea)