
def productoiter (l1, l2):
    res = []
    it1 = iter (l1)
    it2 = iter (l2)
    try:
        while True:
            res.append (it1.next () *
                        it2.next ())
    except StopIteration:
        pass
    return res
