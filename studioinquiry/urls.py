from django.conf.urls.defaults import *
from studioinquiry.views import inquiryAdmin,inquiryDetail,deleteInquiry

urlpatterns = patterns('',
	(r'^inquiry/$',inquiryAdmin),
  	(r'^inquiry/detail_(?P<id>\w+)/$',inquiryDetail),
  	(r'^inquiry/delete_(?P<id>\w+)/$',deleteInquiry),
)	