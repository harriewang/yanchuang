#coding:utf-8
from django.db import models
from django.utils.translation import ugettext as _
from tinymce import models as tinymce_models

class Placeholder(models.Model):
	"""Placeholders, we can use lots of boxes to compose a placeholder"""
	
	name        = models.SlugField(_('Placeholder Name'), unique=True, max_length=100, help_text=_('Used as a hook in the template (Letters, numbers, underscores and hyphens only).'))
	description = models.CharField(_('Placeholder Description'), max_length=200, blank=True)
	active      = models.BooleanField(_('Actived'), default=True)
	boxes       = models.ManyToManyField('Box', blank=True)
	
	class Meta:
		verbose_name_plural = _('Placeholders')
		ordering = ['name',]
	
	def __unicode__(self):
		return self.name
		
class Box(models.Model):
	"""Placeholder Boxes"""
	
	name         = models.SlugField(_('Box Name'), unique=True, max_length=100, help_text=_('Used as a hook in the template (Letters, numbers, underscores and hyphens only).'))
	description  = models.CharField(_('Box Description'), max_length=200, blank=True)
	content      = tinymce_models.HTMLField(_('Box Content'), blank=True)
	weight       = models.IntegerField(_('Weight'), default=0)
	active       = models.BooleanField(_('Actived'), default=True)
	placeholders = models.ManyToManyField('Placeholder', blank=True)
	
	class Meta:
		verbose_name_plural = _('Placeholder Boxes')
		ordering = ['weight','name']
	
	def __unicode__(self):
		return self.name
