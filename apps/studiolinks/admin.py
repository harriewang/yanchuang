#coding:utf-8

from django.contrib import admin
from models import StudioLink

class StudioLinkAdmin(admin.ModelAdmin):
    pass

admin.site.register(StudioLink,StudioLinkAdmin)