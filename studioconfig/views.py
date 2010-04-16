# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from models import StudioConfig
from forms import ConfigForms

def studioConfig(request):
	user=request.session.get('Studio_Login_Key',None)
	if not user:
		return HttpResponseRedirect('/studio/admin/login/')
	else:
		c=StudioConfig.objects.get(id=1)
		current_data = {'title':c.title,'description':c.description,'keywords':c.keywords}
		form =ConfigForms(initial=current_data)
		if request.method=='POST':
			form=ConfigForms(request.POST)
			if form.is_valid():
				c.title=form.cleaned_data['title']
				c.description=form.cleaned_data['description']
				c.keywords=form.cleaned_data['keywords']
				c.save()
				return HttpResponseRedirect('/studio/admin/config/')
		return render_to_response('admin/config.html',{'form':form})