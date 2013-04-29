
class A (object):
    pass

class B (object):
    pass

class AB (A, B):
    pass

class BA (B, A):
    pass

class D (AB, BA):
    pass
