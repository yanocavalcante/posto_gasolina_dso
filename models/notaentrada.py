from models.nota import Nota


class NotaEntrada(Nota):
    def __init__(self,produtos: list, num: str, caixa, valor: float, fornecedor: str):
        super().__init__(produtos, num, caixa, valor)
        self.__fornecedor = fornecedor
        