# -*- coding: utf-8 -*-
import os
import sys
import importlib
from setuptools import setup, find_packages

sys.path.insert(0, os.path.join(os.path.abspath('.'), 'sphinxcontrib'))
paradoxy = importlib.import_module('paradoxy')

long_desc = '''
sphinxcontrib.paradoxy is an extension for Sphinx that makes it
very easy to add links to objects of a project documented with
`Doxygen <http://www.doxygen.org>`_.
'''

setup(
    name='sphinxcontrib-paradoxy',
    version=paradoxy.__version__,
    url='https://github.com/fpoirotte/sphinxcontrib-paradoxy',
    download_url='https://github.com/fpoirotte/sphinxcontrib-paradoxy',
    license='BSD',
    author='Francois Poirotte',
    author_email='clicky@erebot.net',
    description='Adds links to Doxygen objects within Sphinx',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation',
    ],
    keywords="sphinx doxygen links",
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Sphinx>=1.3.6',
        'Sphinx<1.6',
        'lxml',
    ],
    test_suite='nose.collector',
    namespace_packages=['sphinxcontrib'],
)
