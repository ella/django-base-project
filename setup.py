from setuptools import setup, find_packages
import djangobaseproject

version = "%d.%d.%d" % djangobaseproject.VERSION

setup(
    name = 'djangobaseproject',
    version = version,
    description = 'Django Base Project',
    long_description = '\n'.join((
        'Django Base Project',
        '',
    )),
    author = 'centrum holdings s.r.o',
    license = 'BSD',

    packages = find_packages(
        where = '.',
        # TODO: exclude settings.py
    ),

    include_package_data = True,

    entry_points={
        'setuptools.file_finders': ['dummy = setuptools_entry:dummylsfiles'],
        # TODO: need to have manage.py executable
        'setuptools.installation': ['eggsecutable = djangobaseproject.manage'],
    },

    install_requires = [
        'setuptools>=0.6b1',
    ],
)
