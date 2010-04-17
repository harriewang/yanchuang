from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	(r'^$','studio.views.index'),
	#(r'^admin/$','studio.views.admin'),
  	(r'^inquiry/$','studio.views.inquiry'),
  	(r'^case/$','studio.views.allCase'),
  	(r'^case/detail_(?P<id>\w+)/$','studio.views.caseDetail'),
  	(r'^news/detail_(?P<id>\w+)/$','studio.views.newsDetail'),
  	(r'^news/$','studio.views.allNews'),
  	(r'^(?P<title>\w+)/$','studio.views.content'),
  	#(r'^admin/',include('studiouser.urls')),
  	#(r'^admin/',include('studioconfig.urls')),
  	#(r'^admin/',include('studiocontent.urls')),
  	#(r'^admin/',include('studionews.urls')),
  	#(r'^admin/',include('studiocase.urls')),
  	#(r'^admin/',include('studioinquiry.urls')),
  	#(r'^admin/',include('studiolink.urls')),
  	
	#(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root' : settings.STATIC_PATH}),
    # Example:
    # (r'^zozs/', include('zozs.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/(.*)', admin.site.root),
)
