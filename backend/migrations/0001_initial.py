# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Backend'
        db.create_table(u'backend_backend', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('backendId', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kind', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('serverIp', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('serverFqdn', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'backend', ['Backend'])


    def backwards(self, orm):
        # Deleting model 'Backend'
        db.delete_table(u'backend_backend')


    models = {
        u'backend.backend': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Backend'},
            'backendId': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'kind': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'serverFqdn': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'serverIp': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'})
        }
    }

    complete_apps = ['backend']