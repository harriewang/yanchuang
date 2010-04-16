from django.conf.urls.defaults import *
from studiocontent.views import addContent,contentList,deleteSiteContent,deleteSubContent,editSiteContent,editSubContent

urlpatterns = patterns('',
	(r'^addcontent/$',addContent),
  	(r'^content/$',contentList),
  	(r'^content/delete_(?P<id>\w+)/$',deleteSiteContent),
  	(r'^content/deletesub_(?P<id>\w+)/$',deleteSubContent),
  	(r'^content/edit_(?P<id>\w+)/$',editSiteContent),
  	(r'^content/editsub_(?P<id>\w+)/$',editSubContent),
)
             