# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'myapp.ip_address'
        db.add_column(u'myapp_myapp', 'ip_address',
                      self.gf('django.db.models.fields.CharField')(default='ABC', max_length=120),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'myapp.ip_address'
        db.delete_column(u'myapp_myapp', 'ip_address')


    models = {
        u'myapp.myapp': {
            'Meta': {'object_name': 'myapp'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'max_length': '120'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['myapp']