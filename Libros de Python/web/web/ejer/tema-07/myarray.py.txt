# -*- coding: utf-8 -*-

"""

  Módulo MyArray

  >>> a = MyArray (3)
  >>> a [2] = 2
  >>> a [2]
  2
  >>> a = MyArray (3)
  >>> a [2] = 2
  >>> a.zero ()
  >>> a [2]
  0
  >>> a = MyArray (3)
  >>> a [1]
  0

"""

from ctypes import *
from ctypes.util import find_library

_lib = cdll.LoadLibrary (find_library ('c'))

_lib.malloc.argtypes = (c_long,)
_lib.malloc.restype  = c_void_p

_lib.free.argtypes = (c_void_p,)

_lib.memset.arg_types = c_void_p, c_int, c_long

class MyArray (object):

    def __init__ (self, size = 0, *a, **k):
        super (MyArray, self).__init__ (*a, **k)
        arrsize = sizeof (c_int) * size
        data = _lib.malloc (c_long (arrsize))
        self._data = cast (data, POINTER(c_int))
        self._size = size
        self.zero ()
        
    def __getitem__ (self, key):
        if key < 0 or key >= self._size:
            raise IndexError
        return self._data[key]
    
    def __setitem__ (self, key, val):
        if key < 0 or key >= self._size:
            raise IndexError
        self._data[key] = val

    def __del__ (self):
        _lib.free (self._data)

    def zero (self):
        _lib.memset (self._data, 0, self._size * sizeof (c_int))

    @property
    def size (self):
        return self._size

if __name__ == '__main__':
    import doctest
    doctest.testmod ()

