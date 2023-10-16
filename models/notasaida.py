from models.nota import Nota
#from cliente import Cliente

class NotaSaida(Nota):
    def __init__(self, num, produtos, cliente):
        super().__init__(num, produtos)
        self.__cliente = cliente
    