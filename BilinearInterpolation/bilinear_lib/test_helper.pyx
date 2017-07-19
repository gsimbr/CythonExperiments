import numpy as np
from . bilinear cimport bilinear_interpolation_c_cython

def python_bilinear_cython_wrapper(
        stripe):
    no_substripes = len(stripe.substripes)
    erg = np.zeros(no_substripes)
    cdef int idx
    for idx in range(no_substripes):
        ss = stripe.substripes[idx]
        erg[idx] = bilinear_interpolation_c_cython(
            ss.q11, ss.q12, ss.q21, ss.q22, ss.x1, ss.x2, ss.y1, ss.y2, ss.x,
            ss.y)
    return erg