#!/usr/bin/env python
import os

from setuptools import setup

setup(
    name = "setuptools-teamcity-test",
    version = "0.1",
    license = "GPL",
    url = "https://github.com/immobilienscout24/teamcity-test-command",
    packages=['teamcity_test'],
    #test_suite = 'test.py',

    author = "Sebastian Herold",
    author_email = "sebastian.herold@immobilienscout24.de",

    description = "This extension to setuptools allows to run tests in a TeamCity compatible form",
    keywords= "teamcity setuptools test",
)

