"""
This performs vecorized operations on both a Python object passed and numpy
arrays in Cython.
"""


import numpy as np
from . bilinear cimport bilinear_interpolation_c_cython
from . bilinear_cython_header cimport BilinearInterpolation

cpdef python_bilinear_cython_wrapper(stripe):
    """
    This performs bilinear interpolation inside a mixed C and Python Hybrid on 
    a Python object carrying info on multiple points on which should be 
    interpolated upon.
    
    :param Stripe stripe: 
    :return: A vector with all the results of bilinear interpolation.
    """
    no_substripes = len(stripe.substripes)
    erg = np.zeros(no_substripes)
    cdef int idx
    for idx in range(no_substripes):
        ss = stripe.substripes[idx]
        erg[idx] = bilinear_interpolation_c_cython(
            ss.q11, ss.q12, ss.q21, ss.q22, ss.x1, ss.x2, ss.y1, ss.y2, ss.x,
            ss.y)
    return erg


cpdef numpy_bilinear_interpol(double[:] q11, double[:] q12,
        double[:] q21, double[:] q22, double[:] x1, double[:] x2,
        double[:] y1, double[:] y2, double[:] x, double[:] y):
    """
    This performs bilinear interpolation on a multiple of data all passed in 
    a numpy array. By far the fastest version, although the data would have to 
    be prepared first.
    
    :param np.array q11: An array of the function value at the lowerleft corner 
        of the tile.
    :param np.array q12: An array of the function value at the lowerright 
        corner of the tile.
    :param np.array q21: An array of the function value at the upperright 
        corner of the tile.
    :param np.array q22: An array of the function value at the upperleft corner 
        of the tile.
    :param np.array x1: An array of the lower x coordinates of the tiles.
    :param np.array x2:  An array of the upper x coordinates of the tiles.
    :param np.array y1: An array of the lower y coordinates of the tiles.
    :param np.array y2: An array of the upper y coordinates of the tiles.
    :param np.array x: An array of the x coordinates on which should be 
        interpolated upon.
    :param np.array y: An array of the x coordinate on which should be 
        interpolated upon.
    :return: An array of the interpolation values of the function at points 
        (x[i],y[i]).
    :rtype: np.array
    """
    cdef int idx
    cdef int no_substripes = len(q11)
    erg = np.zeros(no_substripes, dtype=float)
    for idx in xrange(no_substripes):
        erg[idx] = BilinearInterpolation(
            q11[idx], q12[idx], q21[idx], q22[idx], x1[idx], x2[idx], y1[idx],
            y2[idx], x[idx], y[idx])

    return erg