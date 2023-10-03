from abc import ABC, abstractmethod


class Nota(ABC):
    @abstractmethod
    def __init__(self):
        self.__produtos = []
    
    @property
    def produtos(self):
        return self.__produtos
    
