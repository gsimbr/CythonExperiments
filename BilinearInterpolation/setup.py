from distutils.core import setup, Extension
from Cython.Build import cythonize

requires = [
    'Cython',
    'numpy',
    'scipy',
    'sympy',
    'argparse'
    ]


setup(
    name='Bilinear',
    requires=requires,
    ext_modules=cythonize(
        "bilinear_lib/*.pyx", "bilinear_lib/bilinear_extern.c"),
)
