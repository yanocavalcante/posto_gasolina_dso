from models.nota import Nota
#from cliente import Cliente

class NotaSaida(Nota):
    def __init__(self, num: int, produtos: list, cliente: str):
        super().__init__(num, produtos)
        self.__cliente = cliente
        self.__valor = 0
    
    @property
    def valor(self):
        return self.__valor
    
    def calcula_valor_saida(self):
        self.valor = 0
        for produto in self.produtos:
            self.valor = self.valor + (produto['nome'].preco * produto['qnt'])
        self.valor = self.desconto()

    def desconto(self):
        self.valor = self.valor * ((100-self.cliente.valor_desconto)/100)
        return self.valor