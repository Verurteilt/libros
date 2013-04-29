
from unarygen import unarygen
from itertools import islice

def potencia (fn, val, n):
    return islice (unarygen (fn) (val), n, None).next ()
