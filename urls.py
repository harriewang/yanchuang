from django.conf.urls.defaults import *
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$','studiocontents.views.index'),
    (r'^test/$','studiocontents.views.test'),
    (r'^admin/', include(admin.site.urls)),
    (r'(?P<navigation_slug>[a-z0-9-_]+)/$','studiocontents.views.content'),
    # Example:
    # (r'^yanchuang/', include('yanchuang.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
