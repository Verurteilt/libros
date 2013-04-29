
def estafunciontiraexcepcion ():
    """
    :raise NotImplemented:
    """
    raise NotImplemented
    print "hola"

def may_raise (obj):
    return obj.__doc__.find (':raise') >= 0 or \
           obj.__doc__.find ('@raise') >= 0

