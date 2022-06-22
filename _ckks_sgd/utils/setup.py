import os

from sklearn._build_utils import gen_from_templates
import numpy
from distutils.core import setup, Extension
from Cython.Build import cythonize


if __name__ == "__main__":
    
    libraries = []
    if os.name == "posix":
        libraries.append("m")
        
    templates = [
        "_seq_dataset.pyx.tp",
        "_seq_dataset.pxd.tp",
        "_weight_vector.pyx.tp",
        "_weight_vector.pxd.tp",
    ]

    gen_from_templates(templates,top_path="")
    
    setup(ext_modules = cythonize(Extension(
     "_cython_blas", 
     sources=["_cython_blas.pyx"],
    libraries=libraries,
    extra_compile_args=[],
    extra_link_args=[]
    )))
    
    
    setup(ext_modules = cythonize(Extension(
    "_weight_vector",
    sources=["_weight_vector.pyx"],
    include_dirs=[numpy.get_include()],
    library_dirs=[],
    libraries=libraries,
    extra_compile_args=[],
    extra_link_args=[]
    )))
    
    
    setup(ext_modules = cythonize(Extension(
    "_random",
    sources=["_random.pyx"],
    include_dirs=[numpy.get_include()],
    libraries=libraries,
    extra_compile_args=[],
    extra_link_args=[]
    )))
    
    setup(ext_modules = cythonize(Extension(
    "_seq_dataset",
    sources=["_seq_dataset.pyx"],
    include_dirs=[numpy.get_include()],
    library_dirs=[],
    libraries=[],
    extra_compile_args=[],
    extra_link_args=[]
    )))
    