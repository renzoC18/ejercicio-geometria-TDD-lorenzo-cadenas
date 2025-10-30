import unittest
from src.circulo.circulo import Circulo
from math import pi

class TestCirculo(unittest.TestCase):
    def test_area_con_radio_positivo(self):
        circulo = Circulo(radio=5)
        self.assertAlmostEqual(circulo.area(), pi * 25)

    def test_perimetro_con_radio_positivo(self):
        circulo = Circulo(radio=5)
        self.assertAlmostEqual(circulo.perimetro(), 2 * pi * 5)

    def test_diametro_con_radio_positivo(self):
        circulo = Circulo(radio=5)
        self.assertEqual(circulo.diametro(), 10)

    def test_area_con_radio_negativo(self):
        circulo = Circulo(radio=-5)
        with self.assertRaises(ValueError) as contexto:
            circulo.area()
        self.assertEqual(str(contexto.exception), "El radio debe ser positivo")

    def test_perimetro_con_radio_negativo(self):
        circulo = Circulo(radio=-5)
        with self.assertRaises(ValueError) as contexto:
            circulo.perimetro()
        self.assertEqual(str(contexto.exception), "El radio debe ser positivo")

    def test_diametro_con_radio_negativo(self):
        circulo = Circulo(radio=-5)
        with self.assertRaises(ValueError) as contexto:
            circulo.diametro()
        self.assertEqual(str(contexto.exception), "El radio debe ser positivo")

    def test_area_con_radio_cero(self):
        circulo = Circulo(radio=0)
        with self.assertRaises(ValueError) as contexto:
            circulo.area()
        self.assertEqual(str(contexto.exception), "El radio no puede ser cero")

    def test_perimetro_con_radio_cero(self):
        circulo = Circulo(radio=0)
        with self.assertRaises(ValueError) as contexto:
            circulo.perimetro()
        self.assertEqual(str(contexto.exception), "El radio no puede ser cero")

    def test_diametro_con_radio_cero(self):
        circulo = Circulo(radio=0)
        with self.assertRaises(ValueError) as contexto:
            circulo.diametro()
        self.assertEqual(str(contexto.exception), "El radio no puede ser cero")
