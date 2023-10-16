from models.nota import Nota


class NotaEntrada(Nota):
    def __init__(self, num, produtos, fornecedor):
        super().__init__ (num, produtos)
        self.__fornecedor = fornecedor
        self.__valor = 0
    
    @property
    def valor(self):
        return self.__valor
    
    def calcula_valor_entrada(self):
        for produto in self.produtos:
            self.valor = self.valor - (produto['nome'].custo * produto['qnt'])