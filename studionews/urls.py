from django.conf.urls.defaults import *
from studionews.views import addNews,newsList,deleteNews,editNews

urlpatterns = patterns('',
	(r'^addnews/$',addNews),
  	(r'^news/$',newsList),
  	(r'^news/delete_(?P<id>\w+)/$',deleteNews),
  	(r'^news/edit_(?P<id>\w+)/$',editNews),
)
             