import unittest
from src.rectangulo.rectangulo import Rectangulo

class TestRectangulo(unittest.TestCase):
    def test_area_con_lado_positivo(self):
        rect = Rectangulo(lado_a=5, lado_b=10)
        self.assertEqual(rect.area(), 50)

    def test_perimetro_con_lado_positivo(self):
        rect = Rectangulo(lado_a=5, lado_b=10)
        self.assertEqual(rect.perimetro(), 30)

    def test_area_con_lado_negativo(self):
        rect = Rectangulo(lado_a=-5, lado_b=10)
        with self.assertRaises(ValueError) as contexto:
            rect.area()
        self.assertEqual(str(contexto.exception), "Los lados deben ser positivos")

    def test_perimetro_con_lado_negativo(self):
        rect = Rectangulo(lado_a=5, lado_b=-10)
        with self.assertRaises(ValueError) as contexto:
            rect.perimetro()
        self.assertEqual(str(contexto.exception), "Los lados deben ser positivos")

    def test_area_con_lado_cero(self):
        rect = Rectangulo(lado_a=0, lado_b=10)
        with self.assertRaises(ValueError) as contexto:
            rect.area()
        self.assertEqual(str(contexto.exception), "Un lado no puede ser cero")
        
    def test_perimetro_con_lado_cero(self):
        rect = Rectangulo(lado_a=5, lado_b=0)
        with self.assertRaises(ValueError) as contexto:
            rect.perimetro()
        self.assertEqual(str(contexto.exception), "Un lado no puede ser cero")