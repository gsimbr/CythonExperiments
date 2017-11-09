

cdef extern from "multiply.c":
    void c_multiply (double* array, double multiplier, int m, int n)