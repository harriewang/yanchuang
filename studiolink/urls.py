from django.conf.urls.defaults import *
from studiolink.views import addLink,editLink,deleteLink

urlpatterns = patterns('',
  	(r'^links/$',addLink),
  	(r'^links/editlink_(?P<id>\w+)/$',editLink),
  	(r'^links/deletelink_(?P<id>\w+)/$',deleteLink),
)	