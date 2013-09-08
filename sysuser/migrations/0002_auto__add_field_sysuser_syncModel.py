# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SysUser.syncModel'
        db.add_column(u'sysuser_sysuser', 'syncModel',
                      self.gf('django.db.models.fields.CharField')(default='sync', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SysUser.syncModel'
        db.delete_column(u'sysuser_sysuser', 'syncModel')


    models = {
        u'sysuser.sysuser': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'SysUser'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'insertOrder': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'origin': ('django.db.models.fields.CharField', [], {'default': "'automatic'", 'max_length': '45'}),
            'sidiId': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'unique': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'syncModel': ('django.db.models.fields.CharField', [], {'default': "'sync'", 'max_length': '30'}),
            'userId': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['sysuser']