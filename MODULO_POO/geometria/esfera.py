from math import pi

class Esfera:
    def __init__(self, raio:float, cor:str) -> None:
        self._raio = raio
        self.cor = cor
        # self.pi = 3.1416


    def volume(self):
        volume_calculado = (4/3) * pi * (self._raio ** 3)
        return volume_calculado
    
    def area_superficie(self) -> float:
        area_calculada = 4 * pi * (self._raio ** 2)
        return area_calculada
    
    def imprime_cor(self):
        print(f'A cor da esféra é {self.cor}')
    
    @property
    def raio(self) -> int:
        return self._raio
        
    
    @raio.setter
    def raio(self, novo_raio) -> float:
        if novo_raio < 1:
            print('Valor inválido.')
        else:
            self._raio = novo_raio