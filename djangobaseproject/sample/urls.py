from django.conf.urls.defaults import *

from djangobaseproject.sample import views

urlpatterns = patterns('',
    url(r'^$', views.homepage, name='djangobaseproject-homepage'),
)

