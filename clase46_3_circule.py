class Circulo:
    def __init__(self, radio: float):
        self._radio = radio
    
    @property
    def area(self) -> float:
        return 3.1416 * self._radio ** 2
    
    @property
    def radio(self) -> float:
        return self._radio

    @radio.setter
    def radio(self, valor: float):
        if valor < 0:
            raise ValueError("El radio no puede ser negativo")
        self._radio = valor

circle=Circulo(5)
#print(circle.area)
circle.radio=10
print(circle.area)