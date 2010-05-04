#coding:utf-8
from django.contrib import admin
from models import Placeholder, Box

class PlaceholderAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'active',)
	list_filter  = ('active',)
	filter_horizontal = ('boxes',)
	
	def add_view(self, request, form_url='', extra_context=None):
		exclude = self.exclude
		if request.REQUEST.has_key('_popup'):
			if self.exclude:
				self.exclude += ('boxes',)
			else:
				self.exclude = ('boxes',)
		try:
			return super(PlaceholderAdmin, self).add_view(request, form_url, extra_context)
		finally:
			self.exclude = exclude
	
class BoxAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'active',)
	list_filter  = ('active',)
	filter_horizontal = ('placeholders',)
	
	def add_view(self, request, form_url='', extra_context=None):
		exclude = self.exclude
		if request.REQUEST.has_key('_popup'):
			if self.exclude:
				self.exclude += ('placeholders',)
			else:
				self.exclude =('placeholders',)
		try:
			return super(BoxAdmin, self).add_view(request, form_url, extra_context)
		finally:
			self.exclude = exclude
	
admin.site.register(Placeholder, PlaceholderAdmin)
admin.site.register(Box, BoxAdmin)