#coding:utf-8
from django.contrib import admin
from models import *
from django.utils.translation import get_language

class NavigationInline(admin.TabularInline):
	model = Navigation
	max_num = 2

class NavigationAdmin(admin.ModelAdmin):
	list_display = ('title_%s' % get_language().replace('-','_'), 'parent_navigation', 'position', 'active',)
	list_filter  = ('position', 'active',)
	inlines = [NavigationInline]
	
class NewsAdmin(admin.ModelAdmin):
	date_hierarchy = 'create_time'
	list_display   = ('title_%s' % get_language().replace('-','_'), 'news_type', 'create_time', 'active',)
	list_filter    = ('news_type', 'create_time', 'active',)

class CaseAdmin(admin.ModelAdmin):
	list_display = ('name_%s' % get_language().replace('-','_'), 'url', 'preview', 'complete_time', 'case_category',)
	
class CaseCategoryAdmin(admin.ModelAdmin):
	pass

admin.site.register(Navigation, NavigationAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(Case_Category, CaseCategoryAdmin)
