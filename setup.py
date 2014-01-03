# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()
    from setuptools import setup, find_packages

import os
import sys

long_desc = '''
sphinxcontrib.doxylinks is an extension for Sphinx that makes it
very easy to add links to objects of a project documented with
`Doxygen <http://www.doxygen.org>`_.
'''

setup(
    name='sphinxcontrib-doxylinks',
    version='0.2.0',
    url='https://github.com/fpoirotte/sphinxcontrib-doxylinks',
    download_url='https://github.com/fpoirotte/sphinxcontrib-doxylinks',
    license='BSD',
    author='Francois Poirotte',
    author_email='clicky@erebot.net',
    description='Easy linking to Doxygen objects from Sphinx',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Documentation',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Sphinx>=1.0.7',
        'lxml',
    ],
    use_2to3=True,
)
