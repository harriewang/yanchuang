#coding:utf-8
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from studioconfig.models import StudioConfig
from studiocontent.models import SiteContent, SubContent
from studionews.models import News
from studiocase.models import Case
from studioinquiry.models import Inquiry
from studioinquiry.forms import InquiryForm
from studiolink.models import Link
from django.core.paginator import Paginator,InvalidPage,EmptyPage

siteTitle=StudioConfig.objects.get(id=1)  #草帽工作室title信息，包括：title,keywords,description

links=Link.objects.all() #友情链接
	
"""草帽工作室首页"""
def index(request):
	case=Case.objects.all()[0:3]
	news=News.objects.all()[0:3]
	content=SiteContent.objects.all()
	about=SiteContent.objects.get(title="关于草帽")
	return render_to_response('studio/index.html',{'title':siteTitle,'links':links,'case':case,'news':news,'content':content,"about":about})
	
"""草帽工作室后台首页"""
def admin(request):
	user = request.session.get('Studio_Login_Key',None)
	if not user:
		return HttpResponseRedirect('/admin/login/')
	else:
		return render_to_response('admin/base-admin.html',{'links':links})

"""显示某个具体案例"""
def caseDetail(request,id):
	case=Case.objects.get(id=id)
	return render_to_response('studio/casedetail.html',{'case':case,'title':siteTitle,'links':links})
	
"""显示所有案例"""
def allCase(request):
	allcase=Case.objects.all()
	paginator=Paginator(allcase,4)  # 4 objects per page
	# Make sure page request is an int. If not, deliver first page.
	try:
		page=int(request.GET.get('page','1'))
	except ValueError:
		page=1
	# If page request is out of range, deliver last page of results.
	try:
		pagecase=paginator.page(page)
	except (EmptyPage,InvalidPage):
		pagecase=paginator.page(paginator.num_pages)
	return render_to_response('studio/casedetail.html',{'pagecase':pagecase,'title':siteTitle,'links':links})
	
"""显示网站具体内容"""
def content(request,title):
	content=SiteContent.objects.get(title=title)  
	subcontent=SubContent.objects.filter(sitecontent=content)  #得到该内容的子内容
	return render_to_response('studio/contentdetail.html',{'content':content,'subcontent':subcontent,'title':siteTitle,'links':links})

"""显示所有动态"""
def allNews(request):
	allnews=News.objects.all()
	return render_to_response('studio/news.html',{'allnews':allnews,'title':siteTitle,'links':links})
	
"""显示动态具体内容"""	
def newsDetail(request,id):
	news=News.objects.get(id=id)
	return render_to_response('studio/news.html',{'news':news,'title':siteTitle,'links':links})

"""询价系统"""	
def inquiry(request):
	if request.method=='POST':
		form=InquiryForm(request.POST)
		if form.is_valid():
			name=form.cleaned_data['name']
			tel=form.cleaned_data['tel']
			mobile=form.cleaned_data['mobile']
			email=form.cleaned_data['email']
			budget=form.cleaned_data['budget']
			requirement=form.cleaned_data['requirement']
			i=Inquiry(name=name,tel=tel,mobile=mobile,email=email,budget=budget,requirement=requirement)
			i.save()
			return render_to_response('studio/inquiryok.html')
	else:
		form=InquiryForm()
	return render_to_response('studio/inquiry.html',{'form':form,'title':siteTitle,'links':links})
