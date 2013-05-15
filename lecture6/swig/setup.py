#!/usr/bin/env python

from distutils.core import setup, Extension

setup(
    name='test_add',
    version='1.0',
    description='add test',
    author='Joseph Sheedy',
    author_email='joseph.sheedy@gmail.com',
    url='http://example.com/add_test',
    packages=['test_add'],
    py_modules=['add'],
    ext_modules=[
        Extension('_add', sources=['add.c', 'add.i'])
    ]
)
