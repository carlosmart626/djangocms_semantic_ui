#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from djangocms_semantic_ui import __version__


INSTALL_REQUIRES = [
    'django-cms>=3.2.0',
    'django>=1.8,<1.10',
    'django-sekizai >= 0.4.2',
    'django-appconf',
]

CLASSIFIERS = [
    'Development Status :: 5 - Production/Development',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]

setup(
    name='djangocms-semantic-ui',
    version=__version__,
    description='Column Plugin for django CMS',
    author='Carlos Martínez',
    author_email='carlosmart626@gmail.com',
    url='https://github.com/CarlosMart626/djangocms_semantic_ui',
    packages=[
        'djangocms_semantic_ui',
        'djangocms_semantic_ui.migrations',
    ],
    install_requires=INSTALL_REQUIRES,
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.md').read(),
    include_package_data=True,
    zip_safe=False
)
