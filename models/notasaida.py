from models.nota import Nota
#from cliente import Cliente

class NotaSaida(Nota):
    def __init__(self, caixa, produtos, cliente):
        super().__init__(caixa, produtos)
        self.__cliente = cliente
    