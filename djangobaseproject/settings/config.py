from tempfile import gettempdir
from os.path import dirname, join

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ENABLE_DEBUG_URLS = DEBUG

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = join(gettempdir(), 'djangobaseproject.db')
TEST_DATABASE_NAME = join(gettempdir(), 'djangobaseproject-test.db')
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

# TODO: replace this
# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# init logger
LOGGING_CONFIG_FILE = join(dirname(djangobaseproject.__file__), 'settings', 'logging.ini')

# we want to reset whole cache in test
# until we do that, don't use cache
CACHE_BACKEND = 'dummy://'

