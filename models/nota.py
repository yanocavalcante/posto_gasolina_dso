from abc import ABC, abstractmethod


class Nota(ABC):
    @abstractmethod
    def __init__(self, num, produtos):
        self.__num = num
        self.__produtos = []
        self.__valor = 0
    
    @property
    def num(self):
        return self.__num
    
    @property
    def produtos(self):
        return self.__produtos
    
    @property
    def valor(self):
        return self.__valor

    def calcula_valor_entrada(self):
        self.valor = 0
        for produto in self.produtos:
            self.valor = self.valor - (produto['nome'].custo * produto['qnt'])

    def calcula_valor_saida(self):
        self.valor = 0
        for produto in self.produtos:
            self.valor = self.valor + (produto['nome'].preco * produto['qnt'])