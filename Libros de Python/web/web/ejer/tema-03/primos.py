from itertools import takewhile, count, islice

def sieve ():
    primos = []
    for x in count (2):
        candidatos = takewhile (lambda p: p*p < x, primos)
        if not any (map (lambda p: x % p == 0, candidatos)):
            primos.append (x)
            yield x

if __name__ == '__main__':
    p = sieve ()
    print list (islice (p, 10))
