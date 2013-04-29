# -*- coding: utf-8 -*-

"""

  Módulo de C mcd.

  >>> mcd (6, 9)
  3
  >>> mcd (14, 21)
  7
  >>> mcd (0, 1)
  1

"""

import os
from ctypes import *

_lib = cdll.LoadLibrary (os.getcwd () + '/mcd.so')

mcd = _lib.mcd
mcd.argtypes = c_int, c_int
mcd.restype  = c_int

if __name__ == '__main__':
    import doctest
    doctest.testmod ()

