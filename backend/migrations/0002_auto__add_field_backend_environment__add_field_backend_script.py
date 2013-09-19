# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Backend.environment'
        db.add_column(u'backend_backend', 'environment',
                      self.gf('django.db.models.fields.CharField')(default='empty', max_length=1000),
                      keep_default=False)

        # Adding field 'Backend.script'
        db.add_column(u'backend_backend', 'script',
                      self.gf('django.db.models.fields.CharField')(default='empty', max_length=1000),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Backend.environment'
        db.delete_column(u'backend_backend', 'environment')

        # Deleting field 'Backend.script'
        db.delete_column(u'backend_backend', 'script')


    models = {
        u'backend.backend': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Backend'},
            'backendId': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'environment': ('django.db.models.fields.CharField', [], {'default': "'empty'", 'max_length': '1000'}),
            'kind': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'script': ('django.db.models.fields.CharField', [], {'default': "'empty'", 'max_length': '1000'}),
            'serverFqdn': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'serverIp': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'})
        }
    }

    complete_apps = ['backend']