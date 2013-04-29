
def product1 (l1, l2):
    p = list ()
    for i in range (min (len (l1), len (l2))):
        p.append (l1[i] * l2[i])
    return p

