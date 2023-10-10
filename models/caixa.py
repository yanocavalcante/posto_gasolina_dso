class Caixa:
    def __init__(self, saldo, tipo):
        self.__saldo = saldo
        self.__tipo = tipo

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def tipo(self):
        return self.__tipo