from views.tela_cadastro import TelaCadastros
from views.tela_pessoa import TelaPessoa
from models.cliente import Cliente
from models.funcionario import Funcionario
from time import sleep
class CtrlCadastros:
    def __init__(self, controlador_principal) -> None:
        self.__lista_pessoas = []
        self.__tela_pessoa = TelaPessoa()
        self.__tela_cadastros = TelaCadastros()
        self.__controlador_principal = controlador_principal

    @property
    def lista_pessoas(self):
        return self.__lista_pessoas

    @property
    def tela_pessoa(self):
        return self.__tela_pessoa
    
    def input_opcao_cadastros(self):
        
        opcao = self.__tela_cadastros.mostra_opcoes()
        
        if opcao == 2:
            opcao_pessoa = self.__tela_pessoa.mostra_opcoes_pessoa()
            if opcao_pessoa == 1:
                info_pessoa = self.__tela_pessoa.input_cadastro_pessoa()
                info_pessoa = self.verifica_idade(info_pessoa)
                info_pessoa = self.verifica_funcionario(info_pessoa)
                info_pessoa = self.verifica_cpf(info_pessoa)
                info_pessoa = self.verifica_telefone(info_pessoa)

                if info_pessoa['funcionario'] == 'S':
                    self.lista_pessoas.append(Funcionario(id=0 if self.lista_pessoas == [] else self.lista_pessoas[-1].id + 1,
                                                            nome=info_pessoa['nome'], 
                                                            idade=info_pessoa['idade'], 
                                                            cpf=info_pessoa['cpf'], 
                                                            telefone=info_pessoa['telefone']))
                    self.input_opcao_cadastros()
                else:
                    self.lista_pessoas.append(Cliente(id=0 if self.lista_pessoas == [] else self.lista_pessoas[-1].id + 1,
                                                        nome=info_pessoa['nome'], 
                                                        idade=info_pessoa['idade'], 
                                                        cpf=info_pessoa['cpf'],
                                                        telefone=info_pessoa['telefone']))
                    self.input_opcao_cadastros()

            elif opcao_pessoa == 2:
                print("-"*20)
                self.mostra_lista_pessoas()
                id_para_alterar = self.__tela_cadastros.input_id_para_alterar()
                
                id_para_alterar = self.verifica_id()

                pessoa = self.verifica_existencia_id(id_para_alterar)

                if pessoa == None:
                    self.input_opcao_cadastros()


                nome, idade, cpf, telefone = self.__tela_cadastros.opcao_alterar()
                
                idade = self.verifica_idade(idade)
                cpf = self.verifica_cpf(cpf)
                telefone = self.verifica_telefone(telefone)

                pessoa.nome = nome if nome is not None else nome
                pessoa.idade = idade if idade is not None else idade
                pessoa.cpf = cpf if cpf is not None else cpf
                pessoa.telefone = telefone if telefone is not None else telefone

            elif opcao_pessoa == 4:
                self.mostra_lista_pessoas()
                
                input("Digite qualquer coisa para voltar: ")

                self.__controlador_principal.mostra_tela_principal()

        elif opcao == 3:
            
            self.__controlador_principal.mostra_tela_principal()
        
        
            

    def verifica_idade(self, info_pessoa):
        try:
            info_pessoa['idade'] = int(info_pessoa['idade'])
            return info_pessoa
        except ValueError:
            info_pessoa['idade'] = self.tela_pessoa.input_idade()
            return self.verifica_idade(info_pessoa)
        
    def verifica_funcionario(self, info_pessoa):
        try:
            if info_pessoa['funcionario'] not in ['S', 'N']:
                raise ValueError
            else:
                return info_pessoa
        except ValueError:
            info_pessoa['funcionario'] = self.tela_pessoa.input_funcionario()
            return self.verifica_funcionario(info_pessoa)
        
    def verifica_cpf(self, info_pessoa):
        try:
            if len(info_pessoa['cpf']) != 11:
                raise ValueError
            info_pessoa['cpf'] = int(info_pessoa['cpf'])
            return info_pessoa
        except ValueError:
            info_pessoa['cpf'] = input("Digite um cpf válido: ")
            return self.verifica_cpf(info_pessoa)
        
    def verifica_telefone(self, info_pessoa):
        try:
            if len(info_pessoa['telefone']) != 11:
                raise ValueError
            info_pessoa['telefone'] = int(info_pessoa['telefone'])
            return info_pessoa
        except ValueError:
            info_pessoa['telefone'] = input("Digite um telefone válido: ")
            return self.verifica_telefone(info_pessoa)
        
    def verifica_existencia_id(self, id_para_alterar):
        if self.lista_pessoas == []:
            print("Não existe nenhuma pessoa na lista!")
            return
        for pessoa in self.lista_pessoas:
            if pessoa.id == id_para_alterar:
                return pessoa
            
        id_para_alterar = self.__tela_cadastros.input_id_para_alterar()
        self.verifica_existencia_id(id_para_alterar)
        
    
    def mostra_lista_pessoas(self):
        for pessoa in self.lista_pessoas:
            self.tela_pessoa.mostra_pessoa(pessoa)

    def verifica_id(self):
        try:
            id_para_alterar = int(id_para_alterar)
            return id_para_alterar
        except ValueError:
            id_para_alterar = self.__tela_cadastros.input_id_para_alterar()
            self.verifica_id()