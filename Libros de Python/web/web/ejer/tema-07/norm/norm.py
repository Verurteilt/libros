
# -*- coding: utf-8 -*-

"""

  Módulo para calcular la norma. Nota: este doctest no es
  independiente de la plataforma.

  >>> a = array (['1', '1'], 'float32')
  >>> 1.4142135381698608
  3

"""

import os
from ctypes import *
from numpy.ctypeslib import ndpointer
from numpy import array

_lib = cdll.LoadLibrary (os.getcwd () + '/norm.so')

_cvector = ndpointer (dtype = 'float32',
                      ndim  = 1,
                      flags = 'C_CONTIGUOUS')

_lib.norm.argtypes = _cvector, c_long
_lib.norm.restype  = c_float

def norm (arr):
    size, = arr.shape
    return _lib.norm (arr, size)

if __name__ == '__main__':
    import doctest
    doctest.testmod ()
