#coding:utf-8

from django.contrib import admin
from models import News

class NewsAdmin(admin.ModelAdmin):
	date_hierarchy = 'create_time'
	list_display = ('title', 'create_time')

admin.site.register(News,NewsAdmin)

