from abc import ABC, abstractmethod


class Nota(ABC):
    @abstractmethod
    def __init__(self, num: int, list_prod_nota: list):
        self.__num = num
        self.__list_prod_nota = list_prod_nota
    
    @property
    def num(self):
        return self.__num
    
    @property
    def list_prod_nota(self):
        return self.__list_prod_nota

