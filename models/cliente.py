from models.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, cpf: str, telefone: str, id: int) -> None:
        super().__init__(nome, idade, cpf, telefone, id)
        