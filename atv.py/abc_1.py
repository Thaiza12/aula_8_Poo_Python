from abc_1 import ABC, abstractmethod
import math

#class abstrata
class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        """Método abstrado para calcular a área"""
        pass

    @abstractmethod
    def calcular_perimetro(self):
        """Método abstrato para calcular o perímetro"""
        pass

# Classe concreta circulo que herda de FormaGeometrica
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio =raio

    def calcular_area(self):
        return math.pi * self.raio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

#Classe concreta retangulo que herda de FormaGeometrica
class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
    
#Exemplo de uso
if __name__ == "__main__":
    #Criando instancias das classes concretas
    circulo = Circulo(raio=5)
    retangulo = Retangulo(largura=4, altura=7)

    #Calculando área e perímetro do círculo
    print(f"Área do círculo: {circulo.calcular_area():.2f}")
    print(f"Perímetro do círculo: {circulo.calcular_perimetro():.2f}")

    #Calculando área e perímetro do retângulo
    print(f"Área do retângulo: {retangulo.calcular_area():.2f}")
    print(f"Perímetro do retângulo:{retangulo.calcular_perimetro():.2f}")