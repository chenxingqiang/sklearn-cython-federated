import numpy
from sklearn._build_utils import gen_from_templates
from distutils.core import setup, Extension
from Cython.Build import cythonize

if __name__ == "__main__":
    templates = ["_loss.pyx.tp"]
    gen_from_templates(templates)
    setup(ext_modules = cythonize(Extension(
    "_loss",
    sources=["_loss.pyx"],
    include_dirs=[numpy.get_include()],
    library_dirs=[],
    libraries=[],
    extra_compile_args=[],
    extra_link_args=[]
)))