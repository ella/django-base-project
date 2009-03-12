from os.path import dirname, join

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

import djangobaseproject


admin.autodiscover()


urlpatterns = patterns('',)

if settings.DEBUG:
    urlpatterns += patterns('',
        # serve static files
        (r'^static/djangobaseproject/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': join(dirname(djangobaseproject.__file__), 'static'), 'show_indexes': True }),
    )

urlpatterns += patterns('',
    # Example:
    # (r'^djangobaseproject/', include('djangobaseproject.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/(.*)', admin.site.root),
)
