#coding:utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from forms import AddNewsForm
from models import News
from studiouser.views import checkLogin


#新闻管理页面
def newsList(request):
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
		news=News.objects.all()
		return render_to_response('admin/admin-news.html',{'news':news})
		
#添加新闻
def addNews(request):
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
		if request.method=='POST':
			form=AddNewsForm(request.POST)
			if form.is_valid():
				title=form.cleaned_data['title']
				type=form.cleaned_data['type']
				content=form.cleaned_data['content']
				news=News(title=title,type=type,content=content)
				news.save()
				return HttpResponseRedirect('/admin/news')
		else:
			form=AddNewsForm()
		return render_to_response('admin/addnews.html',{'form':form})

#删除新闻			
def deleteNews(request,id):
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
		n=News.objects.get(id=id)
		n.delete()
		return HttpResponseRedirect('/admin/news')
		
#编辑新闻			
def editNews(request,id):
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
		n=News.objects.get(id=id)
		current_data=n
		if request.method=="POST":
			form=AddNewsForm(request.POST)
			if form.is_valid():
				n.title=form.cleaned_data['title']
				n.type=form.cleaned_data['type']
				n.content=form.cleaned_data['content']
				n.save()
				return HttpResponseRedirect('/admin/news/')
		return render_to_response('admin/editnews.html',{'current_data':current_data})