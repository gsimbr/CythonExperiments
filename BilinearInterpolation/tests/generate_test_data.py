"""
This test various implementation for single function calls to a single
interpolation on random test data.
"""

import random
import time
import numpy as np
import matplotlib.pyplot as plt

from bilinear_lib.bilinear_python import bilinear_interpolation_pure_python
from bilinear_lib.bilinear import bilinear_interpolation_mixed_cython, \
    python_bilinear_cython_wrapper, python_bilinear_c_wrapper


def generate_data(factor=5):
    q11 = factor*random.random()
    q12 = factor * random.random()
    q21 = factor * random.random()
    q22 = factor * random.random()

    x1 = -60000+120000*random.random()
    y1 = -60000 + 120000 * random.random()

    x2 = 0.5*x1 + 60000
    y2 = 0.5 * x1 + 60000

    x = 0.5*(x1+x2)
    y = 0.5*(y1+y2)

    return q11, q12, q21, q22, x1, x2, y1, y2, x, y


def main(test_case, iterations):
    times = np.zeros(iterations)
    total = 0
    res = None
    for i in range(iterations):
        q11, q12, q21, q22, x1, x2, y1, y2, x, y = generate_data()
        if test_case == 1:
            start = time.time()
            res = bilinear_interpolation_pure_python(
                q11, q12, q21, q22, x1, x2, y1, y2, x, y)
            end = time.time()
        elif test_case == 2:
            start = time.time()
            res = bilinear_interpolation_mixed_cython(
                q11, q12, q21, q22, x1, x2, y1, y2, x, y)
            end = time.time()
        elif test_case == 3:
            start = time.time()
            res = python_bilinear_cython_wrapper(
                q11, q12, q21, q22, x1, x2, y1, y2, x, y)
            end = time.time()
        elif test_case == 4:
            start = time.time()
            res = python_bilinear_c_wrapper(
                q11, q12, q21, q22, x1, x2, y1, y2, x, y)
            end = time.time()
        else:
            raise NotImplementedError
        times[i] = end - start
        total += end - start

    print "Mean: {}s".format(np.mean(times))
    print "Min: {:.16}s".format(np.min(times))
    print "Max: {:.16}s".format(np.max(times))
    print "Total:  {}s for {} iterations".format(total, iterations)

    return times, res


if __name__ == '__main__':
    iterations = int(1e6)
    data = np.zeros((iterations, 4), dtype=float)

    ref_data, _ = main(1, iterations)
    ref_data = np.mean(ref_data)
    best_case = 1
    best_data = ref_data

    for case in range(1, 5):
        times, _ = main(case, iterations)
        data[:, case-1] = times
        if np.mean(times) < ref_data:
            best_case = case
            best_data = np.mean(times)

    print "Best case {}: {} Percent of Pure Python implementation".format(
        best_case, best_data/ref_data*100)

    plt.figure()
    plt.boxplot(data)
    my_max = np.max(data)
    plt.ylim((-my_max, 1.3*my_max))
    plt.show()

