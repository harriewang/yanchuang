# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Case_Category'
        db.create_table('studiocontents_case_category', (
            ('description_zh_cn', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description_en', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100, db_index=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('name_zh_cn', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('studiocontents', ['Case_Category'])

        # Adding field 'Case.case_category'
        db.add_column('studiocontents_case', 'case_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studiocontents.Case_Category'], null=True, blank=True), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting model 'Case_Category'
        db.delete_table('studiocontents_case_category')

        # Deleting field 'Case.case_category'
        db.delete_column('studiocontents_case', 'case_category_id')
    
    
    models = {
        'studiocontents.case': {
            'Meta': {'object_name': 'Case'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'case_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studiocontents.Case_Category']", 'null': 'True', 'blank': 'True'}),
            'complete_time': ('django.db.models.fields.DateField', [], {}),
            'description_en': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_zh_cn': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name_zh_cn': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'preview': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'studiocontents.case_category': {
            'Meta': {'object_name': 'Case_Category'},
            'description_en': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_zh_cn': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'name_zh_cn': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'})
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
            'create_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 6, 7, 22, 27, 5, 500000)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'title_zh_cn': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }
    
    complete_apps = ['studiocontents']
