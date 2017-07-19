"""
This is a mere Cython header file to expose Python C functions to be importable
in other Cython files (.pyx) via cimport.

The implementation source is in bilinear.pyx.
"""


cdef double bilinear_interpolation_c_cython(
        double q11, double q12, double q21, double q22, double x1, double x2,
        double y1, double y2, double x, double y)

