from models.dao import DAO


class CaixaDAO(DAO):
    def __init__(self):
        super().__init__('caixas.pkl')

    def add(self, caixa):
        if (isinstance(caixa.nome, str)) and (caixa is not None):
            super().add(caixa.nome, caixa)
    
    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)
        
    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)