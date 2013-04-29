
from contextlib import contextmanager

from itertools import imap

@contextmanager
def fastmap ():
    origmap = __builtins__.map
    __builtins__.map = imap
    yield
    __builtins__.map = origmap

if __name__ == '__main__':
    with fastmap ():
        print map
    print map

