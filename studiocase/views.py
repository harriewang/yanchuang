#coding:utf-8
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from forms import CaseForm
from models import Case
from studiouser.views import checkLogin
import Image

Case_Image='/var/www/virtualhost/zozs/media/caseimage/' #图片上传的目录
"""案例管理，在后台显示所有已添加的案例"""
def caseList(request):
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
		case=Case.objects.all()
		return render_to_response('admin/case.html',{'case':case})

"""添加案例，包括案例名称，案例地址，案例截图，案例说明等内容"""
def addCase(request):
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
		if request.method=='POST':
			form=CaseForm(request.POST,request.FILES)
			if form.is_valid():
				caseName=form.cleaned_data['caseName']
				caseUrl=form.cleaned_data['caseUrl']
				caseTime=form.cleaned_data['caseTime']
				caseCaption=form.cleaned_data['caseCaption']
				caseImage=request.FILES.get('caseImage',None)
				c=Case(caseName=caseName,caseUrl=caseUrl,caseTime=caseTime,caseCaption=caseCaption)
				c.save()
				"""上传图片，生成缩略图"""
				if caseImage:  #判断是否有图片上传
					"""判断图片大小是否超过500K"""
					if caseImage.size>500000:
						return HttpResponse('上传的图片大小不能超过500K')
					"""保存上传的图片，并得到图片的url"""
					imageName='caseimg'+str(c.id)+'.jpg' #将案例名称作为案例图片名
					imageDir=Case_Image+imageName
					image=Image.open(caseImage) #用PIL的Image.open打开上传的图片信息
					image.save("%s" %imageDir,"JPEG",quality=100) #保存图片到caseimage文件夹下
					caseImageUrl="/media/caseimage/%s" %imageName #得到图片的Url
					"""生成缩略图，并得到缩略图url"""
					thumbName="thumb_"+imageName #在文件名前加“thumb”，表明是缩略图文件
					thumbDir=Case_Image+thumbName
					thumb=Image.open("%s" % imageDir) #打开已保存的案例图片
					thumb.thumbnail((220,190),Image.ANTIALIAS) #进行缩略图处理，将图片的高定为180
					thumb.save("%s" % thumbDir,"JPEG",quality=100) #保存缩略图到caseimage文件夹下
					caseThumbUrl="/media/caseimage/%s" %thumbName #得到缩略图的Url
					c.caseImageUrl=caseImageUrl
					c.caseThumbUrl=caseThumbUrl
					c.save()
				else:
					return HttpResponse('您还没有上传案例截图')
				return HttpResponse('添加成功，<a href="/admin/case/">返回</a>')
		else:
			form=CaseForm()
		return render_to_response('admin/addcase.html',{'form':form})
			
def deleteCase(request,id):
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
		c=Case.objects.get(id=id)
		c.delete()
		return HttpResponseRedirect('/admin/case/')

def editCase(request,id):
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
		c=Case.objects.get(id=id)
		currentData=c
		if request.method=='POST':
			caseName=request.POST.get('caseName',None)
			caseUrl=request.POST.get('caseUrl',None)
			caseTime=request.POST.get('caseTime',None)
			caseCaption=request.POST.get('caseCaption',None)
			caseImage=request.FILES.get('caseImage',None)
			"""上传图片，生成缩略图"""
			if caseImage:  #判断是否有图片上传
				"""判断图片大小是否超过500K"""
				if caseImage.size>500000:
					return HttpResponse('上传的图片大小不能超过500K')
				"""保存上传的图片，并得到图片的url"""
				imageName='caseimg'+str(c.id)+'.jpg' #将案例名称作为案例图片名
				imageDir=Case_Image+imageName
				image=Image.open(caseImage) #用PIL的Image.open打开上传的图片信息
				image.save("%s" %imageDir,"JPEG",quality=100) #保存图片到caseimage文件夹下
				caseImageUrl="/media/caseimage/%s" %imageName #得到图片的Url
				"""生成缩略图，并得到缩略图url"""
				thumbName="thumb_"+imageName #在文件名前加“thumb”，表明是缩略图文件
				thumbDir=Case_Image+thumbName
				thumb=Image.open("%s" % imageDir) #打开已保存的案例图片
				thumb.thumbnail((220,""),Image.ANTIALIAS) #进行缩略图处理，将图片的高定为180
				thumb.save("%s" % thumbDir,"JPEG",quality=100) #保存缩略图到caseimage文件夹下
				caseThumbUrl="/media/caseimage/%s" %thumbName #得到缩略图的Url
				c.caseImageUrl=caseImageUrl
				c.caseThumbUrl=caseThumbUrl
			c.caseName=caseName
			c.caseUrl=caseUrl
			c.caseTime=caseTime
			c.caseCaption=caseCaption
			c.save()
			return HttpResponse('修改成功，<a href="/admin/case/">返回</a>')
		else:
			form=CaseForm()
		return render_to_response('admin/editcase.html',{'form':form,'currentData':currentData})