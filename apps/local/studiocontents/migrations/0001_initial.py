# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Navigation'
        db.create_table('studiocontents_navigation', (
            ('content_zh_cn', self.gf('django.db.models.fields.TextField')()),
            ('content_en', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('parent_navigation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studiocontents.Navigation'], null=True, blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100, db_index=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title_zh_cn', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('studiocontents', ['Navigation'])

        # Adding model 'News'
        db.create_table('studiocontents_news', (
            ('content_zh_cn', self.gf('django.db.models.fields.TextField')()),
            ('content_en', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100, db_index=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2010, 6, 5, 0, 43, 7, 570000))),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('news_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title_zh_cn', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('studiocontents', ['News'])

        # Adding model 'Case'
        db.create_table('studiocontents_case', (
            ('complete_time', self.gf('django.db.models.fields.DateField')()),
            ('description_zh_cn', self.gf('django.db.models.fields.TextField')()),
            ('description_en', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100, db_index=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('preview', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('name_zh_cn', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('studiocontents', ['Case'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Navigation'
        db.delete_table('studiocontents_navigation')

        # Deleting model 'News'
        db.delete_table('studiocontents_news')

        # Deleting model 'Case'
        db.delete_table('studiocontents_case')
    
    
    models = {
        'studiocontents.case': {
            'Meta': {'object_name': 'Case'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'complete_time': ('django.db.models.fields.DateField', [], {}),
            'description_en': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_zh_cn': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name_zh_cn': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'preview': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'studiocontents.navigation': {
            'Meta': {'object_name': 'Navigation'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'content_en': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_zh_cn': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent_navigation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studiocontents.Navigation']", 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'title_zh_cn': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'studiocontents.news': {
            'Meta': {'object_name': 'News'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'content_en': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_zh_cn': ('django.db.models.fields.TextField', [], {}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 6, 5, 0, 43, 7, 570000)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'title_zh_cn': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }
    
    complete_apps = ['studiocontents']
