from abc import ABC, abstractmethod


class Nota(ABC):
    @abstractmethod
    def __init__(self, caixa, produtos):
        self.__produtos = []
        self.__caixa = caixa
    
    @property
    def produtos(self):
        return self.__produtos
    
    @property
    def caixa(self):
        return self.__caixa
