class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_saque):  # Funcao pode sacer
        # atribui a variavel uma soma do saldo com o limite, para somar o saldo e limite e ter um valor certo do uso
        disponivel_saque = self.__saldo + self.__limite
        return valor_saque <= disponivel_saque  # retorna verdadeiro se pode ou nao sacar, se esta dentro do limite

    def saca(self, valor):  # Funcao Saca
        if self.__pode_sacar(valor):  # Verifica se pode sacar puxando a funcao privada pode_Sacar
            self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        print("Valor depositado {}, Seu saldo atual é {}".format(valor, self.get_saldo))

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
