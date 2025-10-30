from pydantic import BaseModel

class Rectangulo(BaseModel):
    lado_a: float
    lado_b: float

    def area(self) -> float:
        if self.lado_a < 0 or self.lado_b < 0:
            raise ValueError("Los lados deben ser positivos")
        
        if self.lado_a == 0 or self.lado_b == 0:
            raise ValueError("Un lado no puede ser cero")
        return self.lado_a * self.lado_b

    def perimetro(self) -> float:
        if self.lado_a < 0 or self.lado_b < 0:
            raise ValueError("Los lados deben ser positivos")
        
        if self.lado_a == 0 or self.lado_b == 0:
            raise ValueError("Un lado no puede ser cero")
        return 2 * (self.lado_a + self.lado_b)