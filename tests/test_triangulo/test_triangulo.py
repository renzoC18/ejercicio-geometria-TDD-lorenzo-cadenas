import unittest
from src.triangulo.triangulo import Triangulo

class TestTriangulo(unittest.TestCase):
    def test_area_con_lados_positivos(self):
        triangulo = Triangulo(lado_a=3, lado_b=4, lado_c=5)
        self.assertAlmostEqual(triangulo.area(), 6.0)

    def test_perimetro_con_lados_positivos(self):
        triangulo = Triangulo(lado_a=3, lado_b=4, lado_c=5)
        self.assertEqual(triangulo.perimetro(), 12)

    def test_angulos_con_lados_positivos(self):
        triangulo = Triangulo(lado_a=3, lado_b=4, lado_c=5)
        angulos = triangulo.angulos()
        self.assertAlmostEqual(angulos[0], 36.86989764584401)
        self.assertAlmostEqual(angulos[1], 53.13010235415599)
        self.assertAlmostEqual(angulos[2], 90.0)

    def test_es_equilatero(self):
        triangulo = Triangulo(lado_a=5, lado_b=5, lado_c=5)
        self.assertTrue(triangulo.es_equilatero())
        self.assertFalse(triangulo.es_isosceles())
        self.assertFalse(triangulo.es_escaleno())

    def test_es_isosceles(self):
        triangulo = Triangulo(lado_a=5, lado_b=5, lado_c=8)
        self.assertFalse(triangulo.es_equilatero())
        self.assertTrue(triangulo.es_isosceles())
        self.assertFalse(triangulo.es_escaleno())

    def test_es_escaleno(self):
        triangulo = Triangulo(lado_a=3, lado_b=4, lado_c=5)
        self.assertFalse(triangulo.es_equilatero())
        self.assertFalse(triangulo.es_isosceles())
        self.assertTrue(triangulo.es_escaleno())

    def test_es_rectangulo(self):
        triangulo = Triangulo(lado_a=3, lado_b=4, lado_c=5)
        self.assertTrue(triangulo.es_rectangulo())
        triangulo_no_rectangulo = Triangulo(lado_a=5, lado_b=5, lado_c=5)
        self.assertFalse(triangulo_no_rectangulo.es_rectangulo())

    def test_area_con_lado_negativo(self):
        triangulo = Triangulo(lado_a=-3, lado_b=4, lado_c=5)
        with self.assertRaises(ValueError) as contexto:
            triangulo.area()
        self.assertEqual(str(contexto.exception), "Los lados deben ser positivos")

    def test_perimetro_con_lado_negativo(self):
        triangulo = Triangulo(lado_a=3, lado_b=-4, lado_c=5)
        with self.assertRaises(ValueError) as contexto:
            triangulo.perimetro()
        self.assertEqual(str(contexto.exception), "Los lados deben ser positivos")

    def test_angulos_con_lado_negativo(self):
        triangulo = Triangulo(lado_a=3, lado_b=4, lado_c=-5)
        with self.assertRaises(ValueError) as contexto:
            triangulo.angulos()
        self.assertEqual(str(contexto.exception), "Los lados deben ser positivos")

    def test_area_con_lado_cero(self):
        triangulo = Triangulo(lado_a=0, lado_b=4, lado_c=5)
        with self.assertRaises(ValueError) as contexto:
            triangulo.area()
        self.assertEqual(str(contexto.exception), "Un lado no puede ser cero")

    def test_perimetro_con_lado_cero(self):
        triangulo = Triangulo(lado_a=3, lado_b=0, lado_c=5)
        with self.assertRaises(ValueError) as contexto:
            triangulo.perimetro()
        self.assertEqual(str(contexto.exception), "Un lado no puede ser cero")

    def test_angulos_con_lado_cero(self):
        triangulo = Triangulo(lado_a=3, lado_b=4, lado_c=0)
        with self.assertRaises(ValueError) as contexto:
            triangulo.angulos()
        self.assertEqual(str(contexto.exception), "Un lado no puede ser cero")
