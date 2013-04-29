
from itertools import imap

def tienepar1 (lista):
    return any (imap (lambda x: x%2==0, lista))

if __name__ == '__main__':
    print tienepar1 ([2, 2, 2])
    print tienepar1 ([2, 1, 2])
