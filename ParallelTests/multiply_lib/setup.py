from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy as np

requires = [
    'Cython',
    'numpy',
    'scipy',
    'argparse'
    ]


ext_modules = [
    Extension(
        name="multiply_cython",
        sources=["multiply_cython.pyx"],
        extra_compile_args=['-O3', '-fopenmp'],
        extra_link_args=['-fopenmp'],
    )
]

setup(
    name='multiply',
    requires=requires,
    ext_modules=cythonize(ext_modules),
    include=[np.get_include()],
    package_data={
        'multiply_lib': ['*.pxd']}
)
