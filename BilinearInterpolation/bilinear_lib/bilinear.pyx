
cdef bilinear_interpolation_c_cython(
        double q11, double q12, double q21, double q22, double x1, double x2,
        double y1, double y2, double x, double y):
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


cpdef bilinear_interpolation_mixed_cython(
        double q11, double q12, double q21, double q22, double x1, double x2,
        double y1, double y2, double x, double y):
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