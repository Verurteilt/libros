
def fibonacci ():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

if __name__ == '__main__':
    from itertools import islice
    print list (islice (fibonacci (), 10))


