#!/usr/bin/env python
from distutils.core import setup, Extension

setup(
    name="fficpp",
    ext_modules=[
        Extension("fficpp", ["fficpp.cpp"])
    ],
    author = 'tristan fisher',
    author_email = 'code@tristanfisher.com',
)
