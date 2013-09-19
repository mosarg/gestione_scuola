# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Backend.user'
        db.add_column(u'backend_backend', 'user',
                      self.gf('django.db.models.fields.CharField')(default='root', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Backend.user'
        db.delete_column(u'backend_backend', 'user')


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
            'serverIp': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'user': ('django.db.models.fields.CharField', [], {'default': "'root'", 'max_length': '100'})
        }
    }

    complete_apps = ['backend']