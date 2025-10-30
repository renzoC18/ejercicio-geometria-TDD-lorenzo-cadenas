from pydantic import BaseModel
from math import pi

class Circulo(BaseModel):
    radio: float

    def area(self) -> float:
        if self.radio < 0:
            raise ValueError("El radio debe ser positivo")
        
        if self.radio == 0:
            raise ValueError("El radio no puede ser cero")
        return pi * self.radio ** 2

    def perimetro(self) -> float:
        if self.radio < 0:
            raise ValueError("El radio debe ser positivo")
        
        if self.radio == 0:
            raise ValueError("El radio no puede ser cero")
        return 2 * pi * self.radio
    
    def diametro(self) -> float:
        if self.radio < 0:
            raise ValueError("El radio debe ser positivo")
        
        if self.radio == 0:
            raise ValueError("El radio no puede ser cero")
        return 2 * self.radio
    