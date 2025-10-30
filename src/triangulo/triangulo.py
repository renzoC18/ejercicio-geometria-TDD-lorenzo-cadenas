from pydantic import BaseModel
from math import acos, degrees

class Triangulo(BaseModel):
    lado_a: float
    lado_b: float
    lado_c: float

    def area(self) -> float:
        if self.lado_a < 0 or self.lado_b < 0 or self.lado_c < 0:
            raise ValueError("Los lados deben ser positivos")
        
        if self.lado_a == 0 or self.lado_b == 0 or self.lado_c == 0:
            raise ValueError("Un lado no puede ser cero")
        
        s = (self.lado_a + self.lado_b + self.lado_c) / 2
        return (s * (s - self.lado_a) * (s - self.lado_b) * (s - self.lado_c)) ** 0.5

    def perimetro(self) -> float:
        if self.lado_a < 0 or self.lado_b < 0 or self.lado_c < 0:
            raise ValueError("Los lados deben ser positivos")
        
        if self.lado_a == 0 or self.lado_b == 0 or self.lado_c == 0:
            raise ValueError("Un lado no puede ser cero")
        
        return self.lado_a + self.lado_b + self.lado_c
    
    def angulos(self) -> tuple:
        if self.lado_a < 0 or self.lado_b < 0 or self.lado_c < 0:
            raise ValueError("Los lados deben ser positivos")
        
        if self.lado_a == 0 or self.lado_b == 0 or self.lado_c == 0:
            raise ValueError("Un lado no puede ser cero")
        
        angle_A = degrees(acos((self.lado_b**2 + self.lado_c**2 - self.lado_a**2) / (2 * self.lado_b * self.lado_c)))
        angle_B = degrees(acos((self.lado_a**2 + self.lado_c**2 - self.lado_b**2) / (2 * self.lado_a * self.lado_c)))
        angle_C = 180 - angle_A - angle_B
        
        return (angle_A, angle_B, angle_C)
    
    def es_equilatero(self) -> bool:
        return self.lado_a == self.lado_b == self.lado_c
    
    def es_isosceles(self) -> bool:
        return self.lado_a == self.lado_b != self.lado_c or self.lado_a == self.lado_c != self.lado_b or self.lado_b == self.lado_c != self.lado_a
    
    def es_escaleno(self) -> bool:
        return self.lado_a != self.lado_b and self.lado_a != self.lado_c and self.lado_b != self.lado_c
    
    def es_rectangulo(self) -> bool:
        lados = sorted([self.lado_a, self.lado_b, self.lado_c])
        return abs(lados[0]**2 + lados[1]**2 - lados[2]**2) < 1e-9
    