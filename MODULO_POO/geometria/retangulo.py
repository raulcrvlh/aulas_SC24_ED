class Retangulo:
    def __init__(self, base: float, altura: float) -> None:
        self._base = base
        self._altura = altura
        self.area = 0
        self.perimetro = 0

    def calcular_area(self):
        self.area = self._base * self._altura
        print(self.area)

    def calcular_perimitro(self):
        self.perimetro = 2 * (self._base + self._altura)
        print(self.perimetro)

    @property
    def base(self) -> float:
        return self._base
    
    @property
    def altura(self) -> float:
        return self._altura
    
    @base.setter
    def base(self, nova_base:float) -> None:
        self._base = nova_base

    @altura.setter
    def altura(self, nova_altura:float) -> None:
        self._altura = nova_altura