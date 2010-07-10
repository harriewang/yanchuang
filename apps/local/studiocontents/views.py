# coding:utf-8

from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def test(request):
	cases = Case.objects.all()
	return render_to_response('test.html',{'cases':cases},context_instance=RequestContext(request))
	
def index(request):
	
	cases = Case.objects.filter(active=True)
	
	# Get latest five news.
	news = News.objects.filter(active=True)[:5]
	
	return render_to_response(
		'index.html',
		{
		    'cases': cases,
		    'news' : news,
		},
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
	cases = Case.objects.filter(active=True)
	
	paginator = Paginator(cases, 8) #show 8 cases per page
	
	# Make sure page request is an int. If not, deliver first page
	try:
	    page = int(request.GET.get('page', '1'))
	except ValueError:
	    page = 1
	
	# If page request is out of range, deliver last page.    
	try:
	    cases = paginator.page(page)
	except (EmptyPage, InvalidPage):
	    cases = paginator.page(paginator.num_pages)
	# get category list
	cases_categories = Case_Category.objects.all()
	
	return render_to_response(
		'cases.html',
		{
			'cases'				:cases,
			'cases_categories'	:cases_categories,
		},
		context_instance = RequestContext(request)
	)

def caseDetail(request, case_slug):
	
	case = get_object_or_404(Case, slug=case_slug)
	
	return render_to_response(
		'caseDetail.html',
		{'case':case},
		context_instance = RequestContext(request)
	)
		
	
