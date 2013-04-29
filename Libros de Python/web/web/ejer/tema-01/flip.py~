
def flip (fn):
    return lambda a, b: fn (b, a)

def flip2 (fn):
    def flipped (a, b):
        return fn (b, a)
    return flipped
