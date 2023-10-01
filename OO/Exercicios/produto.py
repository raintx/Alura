class Produto:

    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade
        print(f"Produto com o nome {self.__nome} adicionado, no valor de {self.__preco} com {self.__quantidade} item "
              f"em estoque")

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_quantidade(self):
        return self.__quantidade

    def set_preco(self, preco):
        self.__preco = preco
        print("Preco de definido com sucesso!")

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade
        print("quantidade definida com sucesso!")

    def vender(self, valor):
        self.__quantidade -= valor
        total = self.__preco * valor
        print(f"Voce vendeu {valor}, {self.get_nome()} por {self.get_preco()} cada, somando um total de {total}")
        print("Quantidade atual de {} em estoque: {}".format(self.__nome, self.get_quantidade()))
