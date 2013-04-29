
def trace (fn):
    def traced (*a, **k):
        args  = map (str, a)
        kargs = ['%s=%s'%(a, str(b))
                 for a,b in k.items ()]
        print "Ejecutando: fn (%s)" % \
              ', '.join (args + kargs)
        return fn (*a, **k)
    return traced
