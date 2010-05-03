#coding:utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language

# Create your models here.
class StudioConfig(models.Model):
    """Studio Configs,including title, description, keywords"""

    # Studio Title    
    title_en    = models.CharField(_('Stuido Title_EN'), max_length = 255, blank=True)
    title_zh_cn = models.CharField(_('Studio Title_CN'), max_length = 255, blank=True)

    # Studio description
    description_en    = models.TextField(_('Studio Description_EN'), blank=True)
    description_zh_cn = models.TextField(_('Studio Description_CN'), blank=True)

    # Studio keywords: for search by google,baidu etc.    
    keywords = models.TextField(_('Site Keywords')) #keywords of studio
    
    # whether active,we can get config which is actived, so we can change it without delete old one.
    active = models.BooleanField(_('Actived'), default=False) 

    class Meta:
        verbose_name_plural = _('Studio Configs') #plural name display in the admin

    @property    
    def title(self):
        return getattr(self, 'title_%s' % get_language().replace('-','_'))
    
    @property
    def description(self):
        return getattr(self, 'description_%s' % get_language().replace('-','_'))

    def __unicode__(self):
        return self.title

class StudioLink(models.Model):
    """Studio Friend Links"""

    # Friend Link name    
    name = models.CharField(_('Friend Link Title'), max_length=100)
    
    # Friend Link Url
    url = models.URLField(_('Friend Link URL'),)

    # Friend Link Description
    description = models.TextField(_('Friend Link Description'), blank=True)
    
    # We can control the order of links by weight
    weight = models.IntegerField(_('Weight'), default=0, help_text=_("The friend link's weight, fill in numbers please."))    

    # whether active,we can get links  which is actived.
    active = models.BooleanField(_('Actived'), default=True)
    

    class Meta:
        verbose_name_plural = _('Friend Links') #plural name display in the admin

    def __unicode__(self):
        return self.name        
    
