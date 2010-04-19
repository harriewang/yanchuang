#coding:utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _



# Create your models here.
class News(models.Model):
	NEWS_TYPE_CHOICES = (
		('news',  _('News')),
		('doing', _('In Progress')),
		('done',  _('Done')),
	)
	#News Title
	title = models.CharField(_('News Title'),max_length=200)

	#News Type
	news_type = models.CharField(_('News Type'), max_length=100, choices=NEWS_TYPE_CHOICES)

	#News Content
	content = models.TextField(_('News Content'))
	
	#News Create Time
	create_time = models.DateTimeField(_('Create Time'))

	class Meta:
		verbose_name_plural = _('Studio News')
		ordering = ['-create_time']

	#News Create Date
	def __unicode__(self):
		return self.title
