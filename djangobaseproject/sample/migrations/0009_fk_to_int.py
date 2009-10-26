
from south.db import db
from django.db import models
from djangobaseproject.sample.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'Spam.type'
        db.alter_column('sample_spam', 'type_id', models.IntegerField())
        # and rename
        db.rename_column('sample_spam', 'type_id', 'type')
        
    
    
    def backwards(self, orm):

        # rename first
        db.rename_column('sample_spam', 'type', 'type_id')
        # Changing field 'Spam.type'
        db.alter_column('sample_spam', 'type_id', models.ForeignKey(orm['sample.Type']))
        
    
    
    models = {
        'sample.spam': {
            'Meta': {'unique_together': "(('name','expires'),)"},
            'count': ('models.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expires': ('models.DateTimeField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '255'}),
            'type': ('models.IntegerField', [], {}),
            'weight': ('models.FloatField', [], {})
        },
        'sample.type': {
            'description': ('models.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }
    
    complete_apps = ['sample']
