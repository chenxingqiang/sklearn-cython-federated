import os

import numpy
from distutils.core import setup, Extension
from Cython.Build import cythonize

if __name__ == "__main__":
    
    libraries = []
    if os.name == "posix":
        libraries.append("m")
        
    setup(ext_modules = cythonize(Extension(
    "sgd_fast_guest",
    sources=["_sgd_fast_guest.pyx"],
    include_dirs=[numpy.get_include()],
    library_dirs=[],
    libraries=libraries,
    extra_compile_args=[],
    extra_link_args=[]
)))