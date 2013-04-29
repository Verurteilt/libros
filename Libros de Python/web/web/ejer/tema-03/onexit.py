
from contextlib import contextmanager

@contextmanager
def onexit (func):
    yield
    func ()

def diadios ():
    print "Adios!"

if __name__ == '__main__':
    with onexit (diadios):
        print "Hola!"
