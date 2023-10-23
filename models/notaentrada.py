from models.nota import Nota


class NotaEntrada(Nota):
    def __init__(self, num: int, list_prod_nota: list, fornecedor: str):
        super().__init__ (num, list_prod_nota)
        self.__fornecedor = fornecedor
        self.__valor = 0
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def fornecedor(self):
        return self.__fornecedor
        
    def calcula_valor_entrada(self):
        for produto in self.list_prod_nota:
            self.__valor = self.__valor - (produto['prod'].custo * produto['qnt'])