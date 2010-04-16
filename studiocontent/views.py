#coding:utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from forms import AddContentForm
from models import SiteContent, SubContent
from studiouser.views import checkLogin

def contentList(request):
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
		sitecontent=SiteContent.objects.all()
		subcontent=SubContent.objects.all()
		return render_to_response('admin/content.html',{'sitecontent':sitecontent,'subcontent':subcontent})

def addContent(request):
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
		if request.method=="POST":
			form=AddContentForm(request.POST)
			if form.is_valid():
				title=form.cleaned_data['title']
				parent=form.cleaned_data['parent']
				content=form.cleaned_data['content']
				if parent=="0":
					sitecontent=SiteContent(title=title,content=content)
					sitecontent.save()
				else:
					sitecontent=SiteContent.objects.get(id=parent)
					subcontent=SubContent(sitecontent=sitecontent,title=title,content=content)
					subcontent.save()
				return HttpResponseRedirect('/admin/content/')
		else:
			form=AddContentForm()
		directory=SiteContent.objects.all()
		return render_to_response('admin/addcontent.html',{'form':form,'directory':directory})
			
#删除内容
def deleteSiteContent(request,id):
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
		s=SiteContent.objects.get(id=id)
		s.delete()
		return HttpResponseRedirect('/admin/content/')
		
#删除子内容
def deleteSubContent(request,id):
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
		s=SubContent.objects.get(id=id)
		s.delete()
		return HttpResponseRedirect('/admin/content/')
		
#编辑内容		
def editSiteContent(request,id):
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
		s=SiteContent.objects.get(id=id)
		current_data={'title':s.title,'content':s.content}
		if request.method=="POST":
			form=AddContentForm(request.POST)
			if form.is_valid():
				title=form.cleaned_data['title']
				parent=form.cleaned_data['parent']
				content=form.cleaned_data['content']
				if parent=="0":
					s.title=title
					s.content=content
					s.save()
				else:
					sitecontent=SiteContent.objects.get(id=parent)
					subcontent=SubContent(sitecontent=sitecontent,title=title,content=content)
					subcontent.save()
				return HttpResponseRedirect('/admin/content/')
		else:
			form=AddContentForm()
		directory=SiteContent.objects.all()
		return render_to_response('admin/editcontent.html',{'form':form,'directory':directory,'current_data':current_data})
			
#编辑子内容
def editSubContent(request,id):
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
		s=SubContent.objects.get(id=id)
		parentId=s.sitecontent.id
		current_data=s
		if request.method=="POST":
			form=AddContentForm(request.POST)
			if form.is_valid():
				title=form.cleaned_data['title']
				parent=form.cleaned_data['parent']
				content=form.cleaned_data['content']
				if parent=="0":
					s.delete()
					sitecontent=SiteContent(title=title,content=content)
					sitecontent.save()
				else:
					sitecontent=SiteContent.objects.get(id=parent)
					s.title=title
					s.sitecontent=sitecontent
					s.content=content
					s.save()
				return HttpResponseRedirect('/admin/content/')
		else:
			form=AddContentForm()
		directory=SiteContent.objects.exclude(id=parentId)
		return render_to_response('admin/editsubcontent.html',{'form':form,'directory':directory,'current_data':current_data})