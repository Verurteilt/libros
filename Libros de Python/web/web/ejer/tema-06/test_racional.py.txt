
import unittest
from racional import Racional

class RacionalTest (unittest.TestCase):

    def test_init (self):
        r = Racional ()
        self.assertEqual (r.num, 0)
        self.assertEqual (r.den, 1)

        r = Racional (3, 2)
        self.assertEqual (r.num, 3)
        self.assertEqual (r.den, 2)

    def test_str (self):
        r = Racional ()
        self.assertEqual (str (r),  '(0/1)')
        r = Racional (3, 2)
        self.assertEqual (str (r),  '(3/2)')

    def test_add (self):
        r = Racional () + Racional (3)
        self.assertEqual (r.num, 3)
        self.assertEqual (r.den, 1)

        r = Racional (3, 2) + Racional (3)
        self.assertEqual (r.num, 9)
        self.assertEqual (r.den, 2)

    def test_entero (self):
        r = Racional (6, 2)
        self.assertEqual (r.entero, 3)

        r = Racional (6, 7)
        self.assertRaises (ValueError, lambda: r.entero)


