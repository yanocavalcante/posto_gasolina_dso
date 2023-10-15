from models.nota import Nota


class NotaEntrada(Nota):
    def __init__(self, caixa, produtos, fornecedor):
        super().__init__(caixa, produtos)
        self.__fornecedor = fornecedor
        