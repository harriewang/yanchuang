from django.conf.urls.defaults import *
from studiocase.views import addCase,caseList,deleteCase,editCase

urlpatterns = patterns('',
	(r'^addcase/$',addCase),
  	(r'^case/$',caseList),
  	(r'^case/delete_(?P<id>\w+)/$',deleteCase),
  	(r'^case/edit_(?P<id>\w+)/$',editCase),
)
             