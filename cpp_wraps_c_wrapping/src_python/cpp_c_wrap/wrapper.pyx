

cdef class PyStringClass:
    cdef StringClass* thisptr
    def __cinit__(self, str stringi):
        self.thisptr = new StringClass(stringi)


    def get_string_length(self):
        return self.thisptr.getStringLength()


    def __dealloc__(self):
        del self.thisptr