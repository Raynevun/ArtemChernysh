#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='beacon',
      version='1.0.0',
      scripts=['bin/summarize-beacon', 'beacon/helper.py'],
      packages=find_packages()
      )
