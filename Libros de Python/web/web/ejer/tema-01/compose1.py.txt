
def compose (*funcs):
    def composed (x):
        for f in reversed (funcs):
            x = f (x)
        return x
    return composed
