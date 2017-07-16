cdef extern from "bilinear_extern.c":
    double BilinearInterpolation(
    double q11, double q12, double q21, double q22, double x1, double x2,
    double y1, double y2, double x, double y)