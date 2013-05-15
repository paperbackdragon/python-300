#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


ext_1 = Extension("cy_add",   ["cy_add.pyx"])
ext_2 = Extension("cy_add_2", ["cy_add_2.pyx"])
ext_3 = Extension("cy_add_3", ["cy_add_3.pyx", "add.c"])


setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [ext_1,
                   ext_2,
                   ext_3,]
)

