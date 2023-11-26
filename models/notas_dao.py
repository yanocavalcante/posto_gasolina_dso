from models.dao import DAO


class NotasDAO(DAO):
    def __init__(self):
        super().__init__('notas.pkl')

    def add(self, nota):
        if (isinstance(nota.num, int)) and (nota is not None):
            super().add(nota.num, nota)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
