class Caixa:
    def __init__(self, saldo, banco, credito):
        self.__saldo = saldo
        self.__banco = banco
        self.__credito = credito

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def banco(self):
        return self.__banco
    
    @property
    def credito(self):
        return self.__credito
