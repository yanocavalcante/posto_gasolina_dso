from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, idade: int, cpf: str, telefone: str, id: int) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__telefone = telefone
        self.__id = id


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
    def id(self):
        return self.__id
    
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

    @id.setter
    def id(self, id):
        self.__id = id