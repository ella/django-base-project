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

from djangobaseproject.settings.base import *

# TODO: add if there is some env variable use this instead of config
from djangobaseproject.settings.config import *

# TODO:
# try to import some settings from /etc/

try:
    from djangobaseproject.settings.local import *
except ImportError:
    pass

