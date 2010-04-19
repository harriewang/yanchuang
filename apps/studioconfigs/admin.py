#coding:utf-8

from models import StudioConfig
from django.contrib import admin

class StudioConfigAdmin(admin.ModelAdmin):
    pass

admin.site.register(StudioConfig,StudioConfigAdmin)