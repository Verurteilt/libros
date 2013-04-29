
def product1 (lista1, lista2):
    return map (lambda (a, b): a * b, zip (lista1, lista2))

def product2 (lista1, lista2):
    return [ a*b for a,b in zip (lista1, lista2) ]

from itertools import starmap
from operator import mul

def product3 (lista1, lista2):
    return list (starmap (mul, zip (lista1, lista2)))
