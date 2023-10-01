class Pessoa:

    def __init__(self, nome, idade):
        print("Construindo objeto...{}".format(self))
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    def comparar_idade(self):
        return self.__idade >= 18

    def vefirica(self):
        if self.comparar_idade():
            print("Maior de idade")
        else:
            print("Nenor de idade")
