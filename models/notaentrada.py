from models.nota import Nota


class NotaEntrada(Nota):
    def __init__(self, produtos, fornecedor):
        super().__init__ (produtos)
        self.__fornecedor = fornecedor
        