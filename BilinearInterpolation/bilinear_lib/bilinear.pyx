"""
This provides several cythonized implementations for Bilinear interpolation on
single points.
"""


from . bilinear_cython_header cimport BilinearInterpolation

cdef double bilinear_interpolation_c_cython(
        double q11, double q12, double q21, double q22, double x1, double x2,
        double y1, double y2, double x, double y):
    """
    This is a C implementation of Bilinear implementation, but written in the 
    language of Cython. This has to be wrapped to be called by Python.
    
    :param double q11: The function value at the lowerleft corner of the tile.
    :param double q12: The function value at the lowerright corner of the tile.
    :param double q21: The function value at the upperright corner of the tile.
    :param double q22: The function value at the upperleft corner of the tile.
    :param double x1: The lower x coordinate of the tile.
    :param double x2:  The upper x coordinate of the tile.
    :param double y1: The lower y coordinate of the tile.
    :param double y2: The upper y coordinate of the tile.
    :param double x: The x coordinate on which should be interpolated upon.
    :param double y: The x coordinate on which should be interpolated upon.
    :return: The interpolation value of the function at point (x,y).
    :rtype: double
    """
    cdef double x2x1, y2y1, x2x, y2y, yy1, xx1
    x2x1 = x2 - x1
    y2y1 = y2 - y1
    x2x = x2 - x
    y2y = y2 - y
    yy1 = y - y1
    xx1 = x - x1
    return 1.0 / (x2x1 * y2y1) * (
        q11 * x2x * y2y +
        q21 * xx1 * y2y +
        q12 * x2x * yy1 +
        q22 * xx1 * yy1
    )

def python_bilinear_cython_wrapper(
        double q11, double q12, double q21, double q22, double x1, double x2,
        double y1, double y2, double x, double y):
    """
    This merely wraps the :func:`~.bilinear_interpolation_c_cython` from above
    to make it exposable from Python.

    :param double q11: The function value at the lowerleft corner of the tile.
    :param double q12: The function value at the lowerright corner of the tile.
    :param double q21: The function value at the upperright corner of the tile.
    :param double q22: The function value at the upperleft corner of the tile.
    :param double x1: The lower x coordinate of the tile.
    :param double x2:  The upper x coordinate of the tile.
    :param double y1: The lower y coordinate of the tile.
    :param double y2: The upper y coordinate of the tile.
    :param double x: The x coordinate on which should be interpolated upon.
    :param double y: The x coordinate on which should be interpolated upon.
    :return: The interpolation value of the function at point (x,y).
    :rtype: double
    """
    return bilinear_interpolation_c_cython(
        q11, q12, q21, q22, x1, x2, y1, y2, x, y)


def python_bilinear_c_wrapper(
        double q11, double q12, double q21, double q22, double x1, double x2,
        double y1, double y2, double x, double y):
    """
    This wraps a pure C implementation of BilinearInterpolation as imported in
    a corresponding .pxd file which imported the external C-Code.

    :param double q11: The function value at the lowerleft corner of the tile.
    :param double q12: The function value at the lowerright corner of the tile.
    :param double q21: The function value at the upperright corner of the tile.
    :param double q22: The function value at the upperleft corner of the tile.
    :param double x1: The lower x coordinate of the tile.
    :param double x2:  The upper x coordinate of the tile.
    :param double y1: The lower y coordinate of the tile.
    :param double y2: The upper y coordinate of the tile.
    :param double x: The x coordinate on which should be interpolated upon.
    :param double y: The x coordinate on which should be interpolated upon.
    :return: The interpolation value of the function at point (x,y).
    :rtype: double
    """
    return BilinearInterpolation(
        q11, q12, q21, q22,  x1,  x2, y1, y2, x, y)


cpdef double bilinear_interpolation_mixed_cython(
        double q11, double q12, double q21, double q22, double x1, double x2,
        double y1, double y2, double x, double y):
    """
    This is a mixed Cython implementation, which can both be exposed to C Code
    and is also callable from Python code. Thus no further wrapping has to be 
    done. Has its benefits as the function call overhead is a significant factor
    here.
    
    :param double q11: The function value at the lowerleft corner of the tile.
    :param double q12: The function value at the lowerright corner of the tile.
    :param double q21: The function value at the upperright corner of the tile.
    :param double q22: The function value at the upperleft corner of the tile.
    :param double x1: The lower x coordinate of the tile.
    :param double x2:  The upper x coordinate of the tile.
    :param double y1: The lower y coordinate of the tile.
    :param double y2: The upper y coordinate of the tile.
    :param double x: The x coordinate on which should be interpolated upon.
    :param double y: The x coordinate on which should be interpolated upon.
    :return: The interpolation value of the function at point (x,y).
    :rtype: double
    """
    cdef double x2x1, y2y1, x2x, y2y, yy1, xx1
    x2x1 = x2 - x1
    y2y1 = y2 - y1
    x2x = x2 - x
    y2y = y2 - y
    yy1 = y - y1
    xx1 = x - x1
    return 1.0 / (x2x1 * y2y1) * (
        q11 * x2x * y2y +
        q21 * xx1 * y2y +
        q12 * x2x * yy1 +
        q22 * xx1 * yy1
    )