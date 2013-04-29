
def product2 (l1, l2):
    p = list ()
    for a, b in zip (l1, l2):
        p.append (a * b)
    return p

from itertools import izip

def product3 (l1, l2):
    p = list ()
    for a, b in izip (l1, l2):
        p.append (a * b)
    return p

def product5 (l1, l2):
    return [ a*b for a,b in zip (l1, l2) ]
