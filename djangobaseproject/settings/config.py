from tempfile import gettempdir
from os.path import join


DEBUG = True
TEMPLATE_DEBUG = DEBUG


DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = join(gettempdir(), 'djangobaseproject.db')
TEST_DATABASE_NAME = join(gettempdir(), 'djangobaseproject-test.db')
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''


# Make this unique, and don't share it with anybody.
SECRET_KEY = '88b-01f^x4lh$-s5-hdccnicekg07)niir2g6)93!0#k(=mfv$'


# TODO: Fix logging
# init logger
#LOGGING_CONFIG_FILE = join(dirname(testbed.__file__), 'settings', 'logger.ini')
#if isinstance(LOGGING_CONFIG_FILE, basestring) and isfile(LOGGING_CONFIG_FILE):
#    logging.config.fileConfig(LOGGING_CONFIG_FILE)


# we want to reset whole cache in test
# until we do that, don't use cache
CACHE_BACKEND = 'dummy://'

