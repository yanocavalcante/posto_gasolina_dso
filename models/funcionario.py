from models.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome: str, idade: int, cpf: str, telefone: str, id: int) -> None:
        super().__init__(nome, idade, cpf, telefone, id)
        self.__desconto = 30
    
    @property
    def desconto(self):
        return self.__desconto