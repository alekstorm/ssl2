from distutils.core import setup
from distutils.extension import Extension

setup(
    name='ssl2',
    description='Fork of the standard library 2.7 ssl module with backports from Python 3.x',
    url='https://github.com/alekstorm/ssl2',
    py_modules=['ssl2'],
    ext_modules=[Extension("_ssl2", ["_ssl2.c"])],
)
