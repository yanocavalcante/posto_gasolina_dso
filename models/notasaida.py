from nota import Nota
#from cliente import Cliente

class NotaSaida(Nota):
    def __init__(self, produtos: list, cliente):
        super().__init__(produtos)
        self.__cliente = cliente
    