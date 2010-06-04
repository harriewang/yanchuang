# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'StudioConfig'
        db.create_table('studioconfigs_studioconfig', (
            ('description_zh_cn', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description_en', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('keywords', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title_zh_cn', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('studioconfigs', ['StudioConfig'])

        # Adding model 'StudioLink'
        db.create_table('studioconfigs_studiolink', (
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('studioconfigs', ['StudioLink'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'StudioConfig'
        db.delete_table('studioconfigs_studioconfig')

        # Deleting model 'StudioLink'
        db.delete_table('studioconfigs_studiolink')
    
    
    models = {
        'studioconfigs.studioconfig': {
            'Meta': {'object_name': 'StudioConfig'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_zh_cn': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title_zh_cn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'studioconfigs.studiolink': {
            'Meta': {'object_name': 'StudioLink'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }
    
    complete_apps = ['studioconfigs']
