import os, sys
from os.path import dirname, basename, join, pardir

django_settings_module = 'djangobaseproject.settings'
pythonpath = [
    join(dirname(__file__), pardir),
]

sys.path = pythonpath + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = django_settings_module

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

# vim: set ft=python:
