
from ctypes import *
from ctypes.util import find_library
from numpy.ctypeslib import ndpointer, as_ctypes
from numpy import array, ascontiguousarray

_lib = cdll.LoadLibrary (find_library ('c'))

_ptrtype = ndpointer (ndim  = 1,
                      flags = 'C_CONTIGUOUS')
_cmptype = CFUNCTYPE (c_int, c_void_p, c_void_p)
_lib.qsort.argtypes = _ptrtype, c_long, c_long, _cmptype

def _cmpelem (a, b):
    return cmp (a[0], b[0])

def arrsort (arr):
    base_ptr = POINTER (as_ctypes (arr)._type_)
    functype = CFUNCTYPE (c_int, base_ptr, base_ptr)
    
    nmemb, = arr.shape
    size,  = arr.strides
    cmpfun = functype (_cmpelem)
    _lib.qsort (arr, nmemb, size, cast (cmpfun, _cmptype))

if __name__ == '__main__':
    a = array ([3., 2., 1.], dtype='float32')
    print a
    arrsort (a)
    print a
