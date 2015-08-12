from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

#following args are helpful for production - set in the makefile
#comp_args=["-O3", "-ffast-math"]
comp_args=[]
extensions =[
        Extension("*", ["*.pyx"], extra_compile_args=comp_args)
]

setup(
    # compile all pyx files in the pwd
    name = "ffi4wd cython",
    ext_modules = cythonize(extensions),
)
