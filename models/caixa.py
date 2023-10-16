class Caixa:
    def __init__(self, tipo, nome, saldo, credito = None):
        self.__saldo = saldo
        self.__tipo = tipo
        self.__nome = nome
        self.__credito = credito
        self.__listamovimentos = []

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def credito(self):
        return self.__credito
    
    @property
    def listamovimentos(self):
        return self.__listamovimentos

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo


    def calcula_novo_saldo(self, nota):
        self.__saldo += nota.valor
