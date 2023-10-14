from abc import ABC, abstractmethod


class Nota(ABC):
    @abstractmethod
    def __init__(self, produtos, num, caixa, valor):
        self.__produtos = []
        self.__num = num
        self.__caixa = caixa
        self.__valor = valor
    
    @property
    def produtos(self):
        return self.__produtos
    
    @property
    def num(self):
        return self.__num
    
    @property
    def caixa(self):
        return self.__caixa
    
    @property
    def valor(self):
        return self.__valor
