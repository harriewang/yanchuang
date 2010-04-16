#coding:utf-8
from django import forms

class AddUserForm(forms.Form):
	email=forms.EmailField(label="Email",required=True)
	username=forms.CharField(label="用户名",required=True)
	password=forms.CharField(label="密码",required=True,widget=forms.PasswordInput)
	
class LoginForm(forms.Form):
	email=forms.EmailField(label="Email",required=True)
	password=forms.CharField(label="密码",required=True,widget=forms.PasswordInput)
	