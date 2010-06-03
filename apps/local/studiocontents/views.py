# coding:utf8

from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from models import *


def test(request):
	cases = Case.objects.all()
	return render_to_response('test.html',{'cases':cases},context_instance=RequestContext(request))
	
def index(request):
	
	cases = Case.objects.all()
	
	return render_to_response(
		'index.html',
		{'cases':cases},
		context_instance = RequestContext(request)
	)
	
def content(request, navigation_slug):
	
	content = get_object_or_404(Navigation, slug=navigation_slug)
	
	return render_to_response(
		'content.html',
		{'content':content},
		context_instance = RequestContext(request)
	)
	
def cases(request):
	cases = Case.objects.all()
	
	return render_to_response(
		'cases.html',
		{'cases':cases},
		context_instance = RequestContext(request)
	)
		
	
