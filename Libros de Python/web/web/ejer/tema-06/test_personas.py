
import unittest
from StringIO import StringIO

from personas import Alumno

class AlumnoTest (unittest.TestCase):

    def test_init (self):
        a = Alumno (nombre="pepe", curso="1")
        self.assertEqual (a.nombre, "pepe")
        self.assertEqual (a.curso, "1")
        

class AlumnoIOTest (unittest.TestCase):

    def setUp (self):
        self.file = StringIO(
            "alumno1\ncurso1\nalumno2\ncurso2\nalumno3\ncurso3")

    def test_uno (self):
        a = Alumno ()
        a.lee_datos (self.file)
        self.assertEqual (a.nombre, "alumno1")
        self.assertEqual (a.curso, "curso1")

    def test_dos (self):
        a = Alumno ()
        a.lee_datos (self.file)
        self.assertEqual (a.nombre, "alumno1")
        self.assertEqual (a.curso, "curso1")
        a = Alumno ()
        a.lee_datos (self.file)
        self.assertEqual (a.nombre, "alumno2")
        self.assertEqual (a.curso, "curso2")
