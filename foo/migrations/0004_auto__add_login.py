# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Login'
        db.create_table('foo_login', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('foo', ['Login'])


    def backwards(self, orm):
        # Deleting model 'Login'
        db.delete_table('foo_login')


    models = {
        'foo.emailer': {
            'Meta': {'object_name': 'Emailer'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sender_email': ('django.db.models.fields.EmailField', [], {'default': "'david.rae@vmsuk.com'", 'max_length': '75'}),
            'sender_name': ('django.db.models.fields.CharField', [], {'default': "'sender'", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'foo.foo': {
            'Meta': {'object_name': 'Foo'},
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        'foo.login': {
            'Meta': {'object_name': 'Login'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['foo']