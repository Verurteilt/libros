
class Racional (object):
    
    __slots__ = 'num', 'den'

    def __init__ (self, num = 0, den = 1, *a, **k):
        super (Racional, self).__init__ (*a, **k)
        self.num = num
        self.den = den

    def __add__ (a, b):
        return Racional (b.num + a.num, b.den) \
               if b.den == a.den else \
               Racional (b.num * a.den + a.num * b.den,
                         b.den * a.den)

    def __sub__ (a, b):
        return a + Racional (-1) * b

    def __mul__ (a, b):
        return Racional (a.num * b.num,
                         a.den * b.den)

    def __div__ (a, b):
        return a * Racional (b.den, b.num)

    def __str__ (self):
        return '(%i/%i)' % (self.num, self.den)
