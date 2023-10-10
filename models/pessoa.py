

class Pessoa:
    def __init__(self, nome: str, idade: int, cpf: str, telefone: str, funcionario: bool) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__telefone = telefone
        self.__funcionario = funcionario


    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def idade(self) -> int:
        return self.__idade
    
    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def telefone(self) -> str:
        return self.__telefone
    
    @property
    def funcionario(self) -> bool:
        return self.__funcionario
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @funcionario.setter
    def funcionario(self, funcionario):
        self.__funcionario = funcionario