
def product1 (l1, l2):
    """

    Devuelve una lista con los productos de los elementos de las
    listas.

    :param l1: Primera lista.
    :param l2: Segunda lista.

    :return: La lista con los productos de los elementos de las
    listas.
    
    """
    
    p = list ()
    for i in range (min (len (l1), len (l2))):
        p.append (l1[i] * l2[i])
    return p
