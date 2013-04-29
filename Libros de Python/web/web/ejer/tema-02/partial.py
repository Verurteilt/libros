
class partial (object):

    def __init__ (self, func, *args, **kwargs):
        self.func   = func
        self.args   = args
        self.kwargs = kwargs

    def __call__ (self, *a, **k):
        a = self.args + a
        k.update (self.kwargs)
        return self.func (*a, **k)

if __name__ == '__main__':
    from operator import add
    print partial (add, 1) (2)
