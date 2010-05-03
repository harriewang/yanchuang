#coding:utf-8

from models import StudioConfig, StudioLink
from django.contrib import admin
from django.utils.translation import get_language

class StudioConfigAdmin(admin.ModelAdmin):
    list_display   = ('title_%s' % get_language().replace('-','_'), 'description_%s' % get_language().replace('-','_'), 'keywords', 'active',)

class StudioLinkAdmin(admin.ModelAdmin):
    list_display   = ('name', 'description', 'url', 'weight', 'active',)
    list_filter    = ('weight', 'active',)
    search_fields  = ('name', 'weight',)


admin.site.register(StudioConfig, StudioConfigAdmin)
admin.site.register(StudioLink, StudioLinkAdmin)