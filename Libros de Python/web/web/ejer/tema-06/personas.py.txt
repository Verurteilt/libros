#!/usr/bin/env python

import sys

class Persona (object):

    def __init__ (self, nombre = '', *a, **k):
        super (Persona, self).__init__ (*a, **k)
        self.nombre = nombre

    def lee_datos (self, fich):
        self.nombre = fich.readline ().strip ()

    def imprime_datos (self):
        print '---'
        print self.__class__.__name__
        print "Nombre:", self.nombre

class Alumno (Persona):

    def __init__ (self, curso = 1, *a, **k):
        super (Alumno, self).__init__ (*a, **k)
        self.curso = curso

    def lee_datos (self, fich):
        super (Alumno, self).lee_datos (fich)
        self.curso = fich.readline ().strip ()

    def imprime_datos (self):
        super (Alumno, self).imprime_datos ()
        print "Curso:", self.curso

class Profesor (Persona):

    def __init__ (self, departamento = '', *a, **k):
        super (Profesor, self).__init__ (*a, **k)
        self.departamento = departamento

    def lee_datos (self, fich):
        super (Profesor, self).lee_datos (fich)
        self.departamento = fich.readline ().strip ()

    def imprime_datos (self):
        super (Profesor, self).imprime_datos ()
        print "Departamento:", self.departamento

def lee_persona (fichero):
   pers = globals ()[fichero.readline ().strip ().capitalize ()] ()
   pers.lee_datos (fichero)
   return pers

if __name__ == '__main__':
    if len (sys.argv) != 3:
        print "Uso: personas.py fichero <tipo>"
        sys.exit (1)

    fichero = open (sys.argv [1])
    filtro  = globals () [sys.argv [2].capitalize ()]

    nperson = int (fichero.readline ())
    personas = [ lee_persona (fichero) for i in range (nperson) ]
    for p in personas:
        if p.__class__ == filtro:
            p.imprime_datos ()
