#coding:utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class StudioConfig(models.Model):

    title = models.CharField(_('Site Title'), max_length = 255) #title of studio
    description = models.TextField(_('Site Description')) #description of studio
    keywords = models.TextField(_('Site Keywords')) #keywords of studio

    class Meta:
        verbose_name_plural = _('Studio Configs') #plural name display in the admin

    def __unicode__(self):
        return self.title
    
    
