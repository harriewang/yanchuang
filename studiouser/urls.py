from django.conf.urls.defaults import *
from studiouser.views import addUsers,logIn,logOut,deleteUser

urlpatterns = patterns('',
	(r'^user/$',addUsers),
  	(r'^login/$',logIn),
  	(r'^logout/$',logOut),
  	(r'^user/deleteuser_(?P<id>\w+)/$',deleteUser),
)
             