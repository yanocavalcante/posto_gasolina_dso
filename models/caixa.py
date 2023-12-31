class Caixa:
    def __init__(self, tipo: str, nome: str, saldo: float, credito = None) -> None:
        self.__saldo = saldo
        self.__saldo_inicial = saldo
        self.__tipo = tipo
        self.__nome = nome
        self.__credito = credito
        self.__listamovimentos = []

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def saldo_inicial(self):
        return self.__saldo_inicial
    
    @saldo_inicial.setter
    def saldo_inicial(self, saldo_inicial):
        self.__saldo_inicial = saldo_inicial
    
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
