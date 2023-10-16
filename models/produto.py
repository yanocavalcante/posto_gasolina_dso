

class Produto:
    def __init__(self, categoria: str, nome: str, fornecedor: str, custo: float, preco: float, estoque: int, id: int) -> None:
        self.__categoria = categoria
        self.__nome = nome
        self.__fornecedor = fornecedor
        self.__custo = custo
        self.__preco = preco
        self.__estoque = estoque
        self.__id = id


    @property
    def categoria(self) -> str:
        return self.__categoria
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def fornecedor(self) -> str:
        return self.__fornecedor
    
    @property
    def custo(self) -> float:
        return self.__custo
    
    @property
    def preco(self) -> float:
        return self.__preco
    
    @property
    def estoque(self) -> int:
        return self.__estoque
    
    @property
    def id(self) -> int:
        return self.__id
    
    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @fornecedor.setter
    def fornecedor(self, fornecedor):
        self.__fornecedor = fornecedor

    @custo.setter
    def custo(self, custo):
        self.__custo = custo

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @estoque.setter
    def estoque(self, estoque):
        self.__estoque = estoque