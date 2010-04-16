# Create your views here.
#coding:utf-8
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from forms import AddUserForm,LoginForm
from models import User

#验证登录信息
def checkLogin(request):
	flag=None
	user=request.session.get('Studio_Login_Key',None)
	if not user:
		return flag
	else:
		flag=1
		return flag

#添加后台管理员
def addUsers(request):
	#验证是否有用户登录
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
	#如果用户已登录，继续执行添加用户
		if request.method=="POST":
			form=AddUserForm(request.POST)
			if form.is_valid():
				email=form.cleaned_data['email']
				username=form.cleaned_data['username']
				password=form.cleaned_data['password']
				u=User(email=email,username=username,password=password)
				u.save()
				return HttpResponseRedirect('/admin/user/')
		else:
			form=AddUserForm()
		user=User.objects.all()
		return render_to_response('admin/user.html',{'form':form,'user':user})
		
def logIn(request):
	if request.method=="POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			try:
				user = User.objects.get(email=email)
				if user.password==password:
					request.session['Studio_Login_Key']=user
					request.session['USER_ID']=user.id
					return HttpResponseRedirect('/admin/user/')
				else:
					return HttpResponse('密码不正确')
			except User.DoesNotExist:
				return HttpResponse('该Email不存在')
	else:
		form=LoginForm()
	return render_to_response('admin/login.html',{'form':form})

def logOut(request):
	try:
		del request.session['Studio_Login_Key']
	except KeyError:
		pass
	return HttpResponseRedirect('/admin/login')
	
def deleteUser(request,id):
	if not checkLogin(request):
		return HttpResponseRedirect('/admin/login')
	else:
		user=User.objects.get(id=id)
		user.delete()
		return HttpResponseRedirect('/admin/user/')
	