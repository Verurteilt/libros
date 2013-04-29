
def mymap (fn, lista):
    if not lista:
        return lista
    return [fn (lista [0])] + mymap (fn, lista [1:])

def myreduce2 (fn, lista, st):
    if not lista:
        return st
    return myreduce2 (fn, lista[1:], fn (st, lista[0]))

def myreduce (fn, lista, st=None):
    if st is None:
        st, lista = lista[0], lista[1:]
    return myreduce2 (fn, lista, st)

def myfilter (fn, lista):
    if not lista:
        return lista
    head, tail = lista[0], lista[1:]
    if fn (head):
        return [head] + myfilter (fn, tail)
    return myfilter (fn, tail)
