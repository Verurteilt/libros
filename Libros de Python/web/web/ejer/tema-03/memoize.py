
def memoize (fn):
    table = {}
    def envoltorio (*a):
        try:
            return table [a]
        except KeyError:
            res = fn (*a)
            table [a] = res
            return res
    return envoltorio

@memoize
def sumamemo (n):
    return sum (xrange (n))

if __name__ == '__main__':
    print sumamemo (100000000)
    print sumamemo (100000000)
