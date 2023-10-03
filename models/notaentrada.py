from nota import Nota


class NotaEntrada(Nota):
    def __init__(self,produtos: list, fornecedor: str):
        super().__init__(produtos)
        self.__fornecedor = fornecedor
        