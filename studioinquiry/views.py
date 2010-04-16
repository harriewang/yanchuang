#coding:utf-8
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from forms import InquiryForm
from models import Inquiry
from studiouser.views import checkLogin

"""后台管理询价"""		
def inquiryAdmin(request):
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
		inquiry=Inquiry.objects.all()
		return render_to_response('admin/inquiryadmin.html',{'inquiry':inquiry})

"""查看某个询价的具体信息"""	
def inquiryDetail(request,id):
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
		i=Inquiry.objects.get(id=id)
		return render_to_response('admin/inquirydetail.html',{'inquiry':i})

"""删除某个询价"""
def deleteInquiry(request,id):
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
		i=Inquiry.objects.get(id=id)
		i.delete()
		return HttpResponseRedirect('/admin/inquiry/')