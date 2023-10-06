from abc import ABC, abstractmethod


class Nota(ABC):
    @abstractmethod
    def __init__(self):
        self.__produtos = []
        self.__caixa = caixa
        self.__valor = valor
    
    @property
    def produtos(self):
        return self.__produtos
    
    @property
    def caixa(self):
        return self.__caixa
    
    @property
    def valor(self):
        return self.__valor
