#coding:utf-8
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from forms import LinkForm
from models import Link
from studiouser.views import checkLogin

"""添加友情链接"""
def addLink(request):
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
		if request.method=="POST":
			form=LinkForm(request.POST)
			if form.is_valid():
				linkTitle=form.cleaned_data['linkTitle']
				linkUrl=form.cleaned_data['linkUrl']
				link=Link(linkTitle=linkTitle,linkUrl=linkUrl)
				link.save()
				return HttpResponseRedirect('/admin/links/')
		else:
			form=LinkForm()
		links=Link.objects.all()
		return render_to_response('admin/links.html',{'form':form,'links':links})
	
def editLink(request,id):
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
		link=Link.objects.get(id=id)
		current_data={'linkTitle':link.linkTitle,'linkUrl':link.linkUrl}
		form=LinkForm(initial=current_data)
		if request.method=="POST":
			form=LinkForm(request.POST)
			if form.is_valid():
				link.linkTitle=form.cleaned_data['linkTitle']
				link.linkUrl=form.cleaned_data['linkUrl']
				link.save()
				return HttpResponseRedirect('/admin/links/')
		links=Link.objects.all()
		return render_to_response('admin/links.html',{'form':form,'links':links})
	
def deleteLink(request,id):
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
		link=Link.objects.get(id=id)
		link.delete()
		return HttpResponseRedirect('/admin/links/')