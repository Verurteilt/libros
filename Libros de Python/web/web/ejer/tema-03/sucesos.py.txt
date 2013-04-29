
import random

def sucesos (prob = .5):
    while True:
        yield random.random () < prob

if __name__ == '__main__':
    from itertools import islice
    print list (islice (sucesos (.7), 10))
