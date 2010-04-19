#coding:utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class StudioLink(models.Model):
    """Studio Friend Link"""

    #Friend Link Title    
    link_title = models.CharField(_('Friend Link Title'), max_length=100)

    #Friend Link Url
    link_url = models.URLField(_('Friend Link URL'))

    #Friend Link Description
    link_description = models.TextField(_('Friend Link Description'))

    class Meta:
        verbose_name_plural = _('Friend Links') #plural name display in the admin

    def __unicode__(self):
        return self.link_title
        
    
    

        
