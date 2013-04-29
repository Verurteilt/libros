
def compose (*funcs):
    return lambda x: reduce (lambda x, f: f (x), funcs[::-1], x)
