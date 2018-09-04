#!/usr/bin/env python
# -*- coding: utf-8 -*-

import versiontools_support
from setuptools import setup, find_packages

setup(
    name = 'taiga-contrib-emails-override',
    version = ':versiontools:taiga_contrib_emails_override:',
    description = 'Plugin to override default taiga email templates',
    long_description = 'Plugin to override the default taiga email templates',
    keywords = 'taiga, email, override',
    author = 'Calendarly',
    author_email = '',
    url = 'https://bitbucket.org/calendarlydevs/taiga-contrib-emails-override/',
    license = '',
    install_requires=[],
    include_package_data = True,
    packages = find_packages(),
    setup_requires = [
        'versiontools >= 1.9',
    ],
    classifiers = [
        'Programming Language :: Python'
    ],
)
