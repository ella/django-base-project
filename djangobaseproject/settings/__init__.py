"""
Settings package is acting exactly like settings module in standard django projects.
However, settings combines two distinct things:
  (1) General project configuration, which is property of the project
    (like which application to use, URL configuration, authentication backends...)
  (2) Machine-specific environment configuration (database to use, cache URL, ...)

Thus, we're changing module into package:
  * base.py contains (1), so no adjustments there should be needed to make project
    on your machine
  * config.py contains (2) with sensible default values that should make project
    runnable on most expected machines
  * local.py contains (2) for your specific machine. File your defaults there.
"""
# load base configuration for whole app
from djangobaseproject.settings.base import *

# TODO:
# use some other name than 'config' if there is some env variable?
from djangobaseproject.settings.config import *

# try to import some settings from /etc/
try:
    import sys
    sys.path.insert(0, '/etc/djangobaselibrary')
    from djangobaseproject_config import *
    del sys.path[0]
except ImportError:
    pass

# load any settings for local development
try:
    from djangobaseproject.settings.local import *
except ImportError:
    pass

