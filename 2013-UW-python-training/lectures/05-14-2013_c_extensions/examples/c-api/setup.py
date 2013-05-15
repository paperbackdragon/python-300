from distutils.core import setup, Extension

setup(
    name='Cadd',
    version='1.0',
    description='Test description',
    ext_modules=[Extension('add', sources=['add.c'])],
)

