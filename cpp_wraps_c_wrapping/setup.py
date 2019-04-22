import setuptools
from setuptools.command.build_clib import build_clib

from Cython.Build import cythonize
from Cython.Distutils import build_ext


libtools = (
    "tools", dict(
        sources=["src/c_code.c", "src/cpp_wrap.cpp"],
        include_dirs=["src"],
        extra_compile_args=["-O3", "-std=c++11"],
        language="c++"))


py_wrap = setuptools.Extension(
    "cpp_c_wrap.wrapper",
    sources=["src_python/cpp_c_wrap/wrapper.pyx"],
    depends=["src_python/cpp_c_wrap/*.pxd"],
    include_dirs=["src"],
    libraries=["tools"],
    extra_compile_args=["-O3", "-std=c++11"],
    language="c++")


setuptools.setup(
    name="CppCWrap",
    author="Georg Simbrunner",
    libraries=[libtools],
    cmdclass={'build_clib': build_clib, 'build_ext': build_ext},
    package_dir={"cpp_c_wrap": "src_python/cpp_c_wrap"},
    packages=["cpp_c_wrap"],
    ext_modules=cythonize([py_wrap]))
