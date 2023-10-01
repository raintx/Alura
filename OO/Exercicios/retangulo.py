class Retangulo:

    def __init__(self, largura, altura):
        self.__largura = largura
        self.__altura = altura

    def calcular_area(self):
        return self.__largura * self.__altura

    def calcular_perimetro(self):
        return 2 * self.__altura * self.__largura
