from models.nota import Nota


class NotaEntrada(Nota):
    def __init__(self, num, produtos, fornecedor):
        super().__init__ (num, produtos)
        self.__fornecedor = fornecedor
        