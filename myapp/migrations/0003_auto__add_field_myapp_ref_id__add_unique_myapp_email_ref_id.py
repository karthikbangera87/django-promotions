# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'myapp.ref_id'
        db.add_column(u'myapp_myapp', 'ref_id',
                      self.gf('django.db.models.fields.CharField')(default='ABC', unique=True, max_length=120),
                      keep_default=False)

        # Adding unique constraint on 'myapp', fields ['email', 'ref_id']
        db.create_unique(u'myapp_myapp', ['email', 'ref_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'myapp', fields ['email', 'ref_id']
        db.delete_unique(u'myapp_myapp', ['email', 'ref_id'])

        # Deleting field 'myapp.ref_id'
        db.delete_column(u'myapp_myapp', 'ref_id')


    models = {
        u'myapp.myapp': {
            'Meta': {'unique_together': "(['email', 'ref_id'],)", 'object_name': 'myapp'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'max_length': '120'}),
            'ref_id': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'unique': 'True', 'max_length': '120'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['myapp']