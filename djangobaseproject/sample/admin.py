from django.contrib import admin
from djangobaseproject.sample.models import Spam, Type

admin.site.register([Spam, Type])

