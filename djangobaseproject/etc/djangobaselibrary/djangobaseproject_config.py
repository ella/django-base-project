import os import djangobaselibrary_meta

LOGGING_CONFIG_FILE = '/etc/djangobaselibrary/djangobaseproject_logging.ini'

DEBUG = False
TEMPLATE_DEBUG = DEBUG
ENABLE_DEBUG_URLS = DEBUG

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'djangobaselibrary'
DATABASE_USER = 'djangobaselibrary'
DATABASE_PASSWORD = 'xxxxxxxxxxxxxxxx'
DATABASE_HOST = 'djdb.cent'
DATABASE_OPTIONS = {
    "charset": "utf8",
    "init_command": "SET storage_engine=InnoDB",
}

# TODO: use trail slash
# TODO: maybe use djangobaseproject word in template and set MEDIA_URL in djangobaselibrary_meta
MEDIA_URL = '%s/djangobaseproject' % djangobaselibrary_meta.MEDIA_URL
ADMIN_MEDIA_PREFIX = 'http://i0.cz/django/centrum/admin_media/'

MIDDLEWARE_CLASSES = (
    'djangobaselibrary.legacy.middleware.RedirectLegacyOldPage',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.http.SetRemoteAddrFromForwardedFor',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'djangobaselibrary.middleware.ModEgoMiddleware',
)

CACHE_BACKEND = 'memcached://%s/' % ';'.join((
    'djfe1.cent:11211',
    'djfe2.cent:11211',
    'djbe1.cent:11211',
    'djbe2.cent:11211',
))

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
    'djangobaselibrary.context_processors.auth',
    'django.core.context_processors.request',
    'djangobaselibrary.context_processors.djangobaselibrary',
)

SESSION_COOKIE_DOMAIN = '.centrum.cz'

# environment
os.environ['http_proxy'] = 'http://proxy.cent:3128'

