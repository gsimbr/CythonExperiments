"""
This test various implementations for computing Bilinear interpolation on a
huge number of points by exposing the python data over various interfaces.
"""

import time

import numpy as np

from bilinear_lib.bilinear_python import bilinear_interpolation_pure_python
from generate_test_data import generate_data
from bilinear_lib.test_helper import python_bilinear_cython_wrapper, \
    numpy_bilinear_interpol


class DataContainer(object):
    """
    A simple mock object with random test data.
    """
    def __init__(self):
        q11, q12, q21, q22, x1, x2, y1, y2, x, y = generate_data()
        self.q11 = q11
        self.q12 = q12
        self.q21 = q21
        self.q22 = q22
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.x = x
        self.y = y


class Stripe(object):
    """
    An ovject containing mock objects, on which bilinear interpolation should
    be performed.
    """
    def __init__(self, no_substrips):
        self.substripes = [DataContainer() for i in range(no_substrips)]


def numpy_container_gen_data(no_substripes):
    """
    This generates a numpy array of random data on which should be interpolated
    upon.

    :param int no_substripes: The number of mock objects.
    :return: Arrays with the necessary vectorized data to perform interpolation
        upon.
    """
    q11vec = np.zeros(no_substripes, dtype=float)
    q12vec = np.zeros(no_substripes, dtype=float)
    q21vec = np.zeros(no_substripes, dtype=float)
    q22vec = np.zeros(no_substripes, dtype=float)
    x1vec = np.zeros(no_substripes, dtype=float)
    x2vec = np.zeros(no_substripes, dtype=float)
    y1vec = np.zeros(no_substripes, dtype=float)
    y2vec = np.zeros(no_substripes, dtype=float)
    xvec = np.zeros(no_substripes, dtype=float)
    yvec = np.zeros(no_substripes, dtype=float)

    for idx in range(no_substripes):
        q11vec[idx], q12vec[idx], q21vec[idx], q22vec[idx], x1vec[idx], \
            x2vec[idx], y1vec[idx], y2vec[idx], xvec[idx], \
            yvec[idx] = generate_data()

    return q11vec, q12vec, q21vec, q22vec, x1vec, x2vec, y1vec, y2vec, xvec, \
        yvec


def main(test_case, no_substripes):
    # prep data
    ref = Stripe(no_substripes)
    q11vec, q12vec, q21vec, q22vec, x1vec, x2vec, y1vec, y2vec, xvec, \
    yvec = numpy_container_gen_data(no_substripes)

    start = time.time()
    if test_case == 1:
        erg = np.zeros(no_substripes, dtype=float)
        for idx in range(no_substripes):
            ss = ref.substripes[idx]
            erg[idx] = bilinear_interpolation_pure_python(
                ss.q11, ss.q12, ss.q21, ss.q22, ss.x1, ss.x2, ss.y1, ss.y2,
                ss.x, ss.y)
    elif test_case == 2:
        erg = python_bilinear_cython_wrapper(ref)
    elif test_case == 3:
        erg = numpy_bilinear_interpol(
            q11vec, q12vec, q21vec, q22vec, x1vec, x2vec, y1vec, y2vec, xvec,
            yvec)
    else:
        raise NotImplementedError
    end = time.time()
    print "Time elapsed: {}s".format(end-start)
    return erg, end-start

if __name__ == '__main__':
    iterations = 1000000
    best_case = 1
    _, best_data = main(best_case, iterations)
    ref_data = best_data

    for case in range(2, 4):
        _, current_timing = main(case, iterations)
        if current_timing < best_data:
            best_data = current_timing
            best_case = case

    print "Best case {}: {} Percent of Pure Python implementation".format(
        best_case, best_data/ref_data*100)
