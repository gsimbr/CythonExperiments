import random
import time
import numpy as np

from bilinear_python import bilinear_interpolation_pure_python
from bilinear import bilinear_interpolation_mixed_cython, \
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
    print "Min: {}s".format(np.mean(times))
    print "Max: {}s".format(np.mean(times))
    print "Total:  {}s for {} iterations".format(total, iterations)


if __name__ == '__main__':
    test_case = 2
    iterations = 1000000
    main(test_case, iterations)
