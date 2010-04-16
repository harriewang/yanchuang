from django.conf.urls.defaults import *
from studioconfig.views import studioConfig

urlpatterns = patterns('',
	(r'^config/$',studioConfig),
)
             