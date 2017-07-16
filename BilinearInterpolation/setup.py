from distutils.core import setup
from Cython.Build import cythonize

requires = [
    'Cython',
    'numpy',
    'scipy',
    'sympy',
    'argparse'
    ]


setup(
    name='BilinearInterpolation',
    requires=requires,
    ext_modules=cythonize("bilinear_lib/*.pyx"),
)