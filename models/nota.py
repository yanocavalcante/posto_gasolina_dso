from abc import ABC, abstractmethod


class Nota(ABC):
    @abstractmethod
    def __init__(self, num: int, produtos: list):
        self.__num = num
        self.__produtos = []
    
    @property
    def num(self):
        return self.__num
    
    @property
    def produtos(self):
        return self.__produtos

