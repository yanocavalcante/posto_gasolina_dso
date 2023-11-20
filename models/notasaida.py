from models.nota import Nota

class NotaSaida(Nota):
    def __init__(self, num: int, list_prod_nota: list, cliente):
        super().__init__(num, list_prod_nota)
        self.__cliente = cliente
        self.__valor = 0
    
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
    
    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente
    
    def calcula_valor_saida(self):
        self.valor = 0
        for produto in self.list_prod_nota:
            self.valor = self.valor + (produto['prod'].preco * produto['qnt'])
        self.valor = self.desconto()

    def desconto(self):
        self.valor = self.valor * ((100-self.cliente.valor_desconto)/100)
        return self.valor