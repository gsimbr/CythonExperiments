#!/usr/bin/env python

"""
multiply.pyx and c_multiply.c test code

designed to be run-able with py.test
"""
from __future__ import absolute_import
import time
import pytest
import numpy as np
from .. multiply_lib import multiply_cython


def test_basic():
    a = np.arange(12, dtype=np.float64).reshape((3, 4))
    b = a * 3
    multiply_cython.multiply(a, 3)
    assert np.array_equal(a, b)


def test_wrong_dims():
    a = np.arange(12, dtype=np.float64).reshape((3, 2, 2))
    with pytest.raises(ValueError):
        multiply_cython.multiply(a, 3)


def test_wrong_type():
    a = np.arange(12, dtype=np.float32).reshape((3,4))
    b = a * 3
    with pytest.raises(ValueError):
        multiply_cython.multiply(a, 3)


def test_zero_dims():
    """
    this shouldn't crash!
    """
    a = np.ones( (3, 0), dtype=np.float64)
    b = a.copy()
    multiply_cython.multiply(a, 3) # zero size, shouldn't do anything
    assert np.array_equal(a, b)


def test_extensive():
    a = np.ones((5000, 5000))
    scal = 5.0
    start = time.time()
    b = np.empty(a.shape)
    b[:] = a[:]*scal
    end = time.time()
    ref_time = end-start
    print "Start parallel"
    start = time.time()
    multiply_cython.multiply(a, 5)
    end = time.time()
    parallel_time = end-start
    print "Ref time = {}s".format(ref_time)
    print "Parallel time = {}s".format(parallel_time)
    assert np.array_equal(a, b)
    assert parallel_time < ref_time
