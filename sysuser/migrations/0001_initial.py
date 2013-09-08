# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SysUser'
        db.create_table(u'sysuser_sysuser', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('userId', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sidiId', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('origin', self.gf('django.db.models.fields.CharField')(default='automatic', max_length=45)),
            ('insertOrder', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'sysuser', ['SysUser'])


    def backwards(self, orm):
        # Deleting model 'SysUser'
        db.delete_table(u'sysuser_sysuser')


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
            'userId': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['sysuser']