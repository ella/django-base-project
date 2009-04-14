from setuptools import setup, find_packages
import djangobaseproject

version = "%d.%d.%d" % djangobaseproject.VERSION

# all fields marked with TODO: REPLACE
# must be filled with some meanigful values

setup(
    name = 'djangobaseproject',
    version = version,
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
    url='http://git.netcentrum.cz/projects/django/GIT/django-base-project.git/' # TODO: REPLACE

    packages = find_packages(
        where = '.',
    ),

    include_package_data = True,

    classifiers=[ # TODO: REPLACE
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],

    entry_points={
        'setuptools.file_finders': ['dummy = setuptools_entry:dummylsfiles'],
        # TODO: how to have manage.py executable?
        'setuptools.installation': ['eggsecutable = djangobaseproject.manage'],
    },

    install_requires = [
        'setuptools>=0.6b1',
    ],
)
