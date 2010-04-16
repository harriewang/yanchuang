#coding:utf-8
from django import forms

Budget_Choice = (
	("不限定","不限定"),
	("￥2000以下","￥2000以下"),
	("￥2000~5000","￥2000~5000"),
	("￥5000~10000","￥5000~10000"),
	("￥10000以上","￥10000以上"),
)

class InquiryForm(forms.Form):
	name=forms.CharField(label="姓名(Name)",required=True)
	tel=forms.CharField(label="电话(Tel)",help_text='（请在号码前面加上区号，如：010-12345678）',required=True)
	mobile=forms.CharField(label="手机(mobile)",required=True)
	email=forms.EmailField(label="电子邮件(E-mail)",required=True)
	budget=forms.ChoiceField(label="设计预算(Budget)",choices=Budget_Choice,help_text='（您也可以在设计需求中写明）')
	requirement=forms.CharField(label="设计需求(Requirement)",widget=forms.Textarea,required=True)