from setuptools import setup, find_packages

# all fields marked with TODO: REPLACE
# must be filled with some meanigful values

# must be in sync with djangobaseproject.VERSION
VERSION = (0, 0, 0, 0)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))


setup(
    name = 'djangobaseproject',
    version = __versionstr__,
    description = 'Django Base Project', # TODO: REPLACE
    long_description = '\n'.join(( # TODO: REPLACE
        'Django Base Project',
        '',
        'this project (python module) is meant as a skeleton',
        'for any centrumholdings django based projects',
    )),
    author = 'centrum holdings s.r.o', # TODO: REPLACE
    author_email='devel@centrumholdings.com', # TODO: REPLACE
    license = 'BSD', # TODO: REPLACE
    url='http://git.netcentrum.cz/projects/django/GIT/django-base-project.git/', # TODO: REPLACE

    packages = find_packages(
        where = '.',
        exclude = ('docs', 'tests')
    ),

    include_package_data = True,

    # TODO: REPLACE
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    entry_points = {
        # TODO: how to have manage.py executable?
#        'setuptools.installation': ['eggsecutable = djangobaseproject.manage'],
    },
    install_requires = [
#        'django',
#        'south',
#        'djangobaselibrary',
        'setuptools>=0.6b1',
    ],
    setup_requires = [
        'setuptools_dummy',
    ],

    # TODO: REPLACE
    buildbot_meta_master = {
        'host' : 'cnt-buildmaster.dev.chservices.cz',
        'port' : 10001,
        'branch' : 'automation',
    },
)

