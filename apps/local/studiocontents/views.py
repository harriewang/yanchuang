# coding:utf8

from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Case


def test(request):
	cases = Case.objects.all()
	return render_to_response('test.html',{'cases':cases},context_instance=RequestContext(request))