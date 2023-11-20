from models.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, cpf: str, telefone: str, id: int,
                 email: str, valor_desconto: int) -> None:
        super().__init__(nome, idade, cpf, telefone, id)
        self.__email = email
        self.__valor_desconto = valor_desconto

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def valor_desconto(self):
        return self.__valor_desconto
    
    @valor_desconto.setter
    def valor_desconto(self, valor_desconto):
        self.__valor_desconto = valor_desconto
