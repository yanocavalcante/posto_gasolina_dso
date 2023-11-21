from models.dao import DAO


class ProdutoDAO(DAO):
    def __init__(self):
        super().__init__('produtos.pkl')

    def add(self, produto):
        if (isinstance(produto.id, id)) and (produto is not None):
            super().add(produto.id, produto)
    
    def get(self, key: id):
        if isinstance(key, int):
            return super().get(key)
    
    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)