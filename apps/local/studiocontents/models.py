#coding:utf-8
import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language

from sorl.thumbnail.fields import ImageWithThumbnailsField


class Navigation(models.Model):
	"""Navigations Manager"""

	POSITION_CHOICES = (
		('top',    _('Top')),
		('bottom', _('Bottom')),
	)
	
	# Slug, use in url
	slug          = models.SlugField(max_length=100, unique=True, help_text=_('Letters, numbers, undersocres and hyphens only.'))
	
	# Parent navigation, a ForeignKey to navigaiton self, so we can add unlimited hierarchy of navigations
	parent_navigation = models.ForeignKey('self', verbose_name=_('Parent Navigation'), blank=True, null=True, help_text=_('Choose a parent navigation, leave it empty if you want to add a top navigaiton'))
	
	# Navigation title
	title_en      = models.CharField(_('Navigation Title_EN'), max_length=100, blank=True)
	title_zh_cn   = models.CharField(_('Navigation Title_CN'), max_length=100)
	
	# Navigation content, use tinymce's HTMLField instead of django's TextField 
	content_en    = models.TextField(_('Content_EN'), blank=True)
	content_zh_cn = models.TextField(_('Content_CN'))

	# Navigation position, determin navigation display on the top or bottom navigation
	position      = models.CharField(_('Navigation Position'), max_length=100, choices=POSITION_CHOICES, blank=True)
	
	# Active
	active        = models.BooleanField(_('Actived'), default=True)
	
	class Meta:
		verbose_name_plural = _('Studio Navigations')
    		
	@property
	def title(self):
		"""Get title by current language"""
		return getattr(self, 'title_%s' % get_language().replace('-','_'))
		
	@property
	def content(self):
		"""Get content by current language"""
		return getattr(self, 'content_%s' % get_language().replace('-','_'))
		
	def __unicode__(self):
		return self.title
		
class News(models.Model):
	"""Studio news"""
	
	NEWS_TYPE_CHOICES = (
		('news',  _('News')),
		('doing', _('In Progress')),
		('done',  _('Done')),
	)
	
	slug          = models.SlugField(max_length=100, unique=True, help_text=_('Letters, numbers, undersocres and hyphens only.')) # Slug, use in url
	title_en      = models.CharField(_('News Title_EN'), max_length=200, blank=True)
	title_zh_cn   = models.CharField(_('News Title_CN'), max_length=200)
	news_type     = models.CharField(_('News Type'), max_length=100, choices=NEWS_TYPE_CHOICES)
	content_en    = models.TextField(_('News Content_EN'), blank=True)
	content_zh_cn = models.TextField(_('News Content_CN'))
	create_time   = models.DateTimeField(_('Create Time'), default=datetime.datetime.now())
	active        = models.BooleanField(_('Actived'), default=True)

	class Meta:
		verbose_name_plural = _('Studio News')
		ordering = ['-create_time']

	@property
	def title(self):
		return getattr(self, 'title_%s' % get_language().replace('-','_'))
	
	@property
	def content(self):
		return getattr(self, 'content_%s' % get_language().replace('-','_'))

	def __unicode__(self):
		return self.title

class Case_Category(models.Model):
	"""Case categories"""
	slug              = models.SlugField(max_length=100, unique=True, help_text=_('Letters, numbers, undersocres and hyphens only.'))
	name_en           = models.CharField(_('Category Name_EN'), max_length=100, unique=True)
	name_zh_cn        = models.CharField(_('Category Name_CN'), max_length=100, unique=True)
	description_en    = models.TextField(_('Category Description_EN'), blank=True)
	description_zh_cn = models.TextField(_('Category Description_CN'), blank=True)
	
	class Meta:
		verbose_name_plural = _('Case Categories')
	
	@property
	def name(self):
		return getattr(self, 'name_%s' % get_language().replace('-','_'))
	
	def __unicode__(self):
		return self.name
	
		
class Case(models.Model):
	"""Studio Case"""
	slug                = models.SlugField(max_length=100, unique=True, help_text=_('Letters, numbers, undersocres and hyphens only.'))
	
	# Case category
	case_category       = models.ForeignKey(Case_Category, verbose_name=_('Case Category'), blank=True, null=True)
	
	name_en             = models.CharField(_('Case Name_EN'), max_length=100, blank=True)
	name_zh_cn          = models.CharField(_('Case Name_CN'), max_length=100)
	description_en      = models.TextField(_('Case Description_EN'), blank=True)
	description_zh_cn   = models.TextField(_('Case Description_CN'))
	url                 = models.URLField(_('Case URL'), verify_exists=False)
	preview             = ImageWithThumbnailsField(
							upload_to = 'cases',
							thumbnail = {'size':(240,160), 'options': ['crop']},
							extra_thumbnails = {
								'100_100': {'size':(100,100), 'options': ['crop']},
								'420_300': {'size':(420,300)},
								'210_80': {'size':(210,80), 'options': ['crop']},
							},
							generate_on_save = True,
							null=True,
							blank=True,		
	)
	complete_time       = models.DateField(_('Complete Time'))
	active              = models.BooleanField(_('Actived'), default=True)
	weight              = models.IntegerField(_('Weight'), default=0 )
	
	class Meta:
		verbose_name_plural = _('Studio Cases')
		ordering = ['-complete_time']
		
	@property
	def name(self):
		return getattr(self, 'name_%s' % get_language().replace('-','_'))
	
	@property
	def description(self):
		return getattr(self, 'description_%s' % get_language().replace('-','_'))
	
	def __unicode__(self):
		return self.name
	
	
