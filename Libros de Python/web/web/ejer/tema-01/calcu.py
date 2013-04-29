# -*- coding: utf-8 -*-

from math import sqrt
from operator import add,sub,mul,div,pow

opfns = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div,
    '**' : pow,
    'exit' : exit,
    'sqrt' : sqrt
    }

def calculadora ():
    try:
        while True:
            ops = raw_input ('Operación: ')
            ops = ops.split ()
            try:
                operador  = ops [0] 
                operandos = ops [1:]
                funcion = opfns [operador]
                print funcion (* map (float, operandos))
            except (KeyError, IndexError, ValueError, TypeError):
                print "Orden incorrecta"
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    calculadora ()

