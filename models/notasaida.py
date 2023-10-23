from models.nota import Nota
#from cliente import Cliente

class NotaSaida(Nota):
    def __init__(self, num: int, list_prod_nota: list, cliente: str):
        super().__init__(num, list_prod_nota)
        self.__cliente = cliente
        self.__valor = 0
    
    @property
    def valor(self):
        return self.__valor
    
    def calcula_valor_saida(self):
        self.valor = 0
        for produto in self.list_prod_nota:
            self.valor = self.valor + (produto['prod'].preco * produto['qnt'])
        self.valor = self.desconto()

    def desconto(self):
        self.valor = self.valor * ((100-self.cliente.valor_desconto)/100)
        return self.valor