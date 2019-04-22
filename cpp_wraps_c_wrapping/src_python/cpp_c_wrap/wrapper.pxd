from libcpp.string cimport string


cdef extern from "cpp_wrap.cpp" namespace "wrap":
    pass

cdef extern from "cpp_wrap.hpp" namespace "wrap":
    cdef cppclass StringClass:
        StringClass(const string &stringi)
        unsigned int getStringLength()