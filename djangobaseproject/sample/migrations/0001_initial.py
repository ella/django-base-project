
from south.db import db
from django.db import models
from djangobaseproject.sample.models import *

'''
created via:
./djangobaseproject/manage.py startmigration djangobaseproject.sample initial
'''

class Migration:
    
    def forwards(self, orm):
        "Write your forwards migration here"
        print 'initial migration forwards'
    
    
    def backwards(self, orm):
        "Write your backwards migration here"
        print 'initial migration backwards'
    
    
    models = {
        
    }
    
    
