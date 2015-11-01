import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''
try:
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except IOError:
    CHANGES = ''

version = '0.1dev'

install_requires = [
    'Kotti>=1.0.0',
    'kotti_tinymce',
    'kotti_accounts',
    'kotti_blog',
    'kotti_calendar',
    'kotti_jsonapi',
    'kotti_settings',
    'kotti_velruse',
    'kotti_compass',
    'kotti_dashboard',
]


setup(
    name='xyzzy',
    version=version,
    description="Add on for Kotti",
    long_description='\n\n'.join([README, CHANGES]),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: Public Domain",
    ],
    author='Kotti developers',
    author_email='kotti@googlegroups.com',
    url='https://github.com/umeboshi2/xyzzy',
    keywords='kotti web cms wcms pylons pyramid sqlalchemy bootstrap',
    license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=[],
    dependency_links=[
        'https://github.com/knowah/PyPDF2/archive/master.tar.gz#egg=PyPDF2-1.15dev',
        'https://github.com/repoze/repoze.workflow/archive/master.tar.gz#egg=repoze.workflow-master',
        'https://github.com/umeboshi2/Kotti/archive/master.tar.gz#egg=Kotti-1.2.2-dev',
        'https://github.com/umeboshi2/kotti_jsonapi/archive/master.tar.gz#egg=kotti_jsonapi-master',
        'https://github.com/umeboshi2/kotti_compass/archive/master.tar.gz#egg=kotti_compass-master',
        'https://github.com/umeboshi2/kotti_dashboard/archive/master.tar.gz#egg=kotti_dashboard-master',

    ],
    entry_points={
        'fanstatic.libraries': [
            'xyzzy = xyzzy.fanstatic:library',
        ],
    },
    extras_require={},
)
