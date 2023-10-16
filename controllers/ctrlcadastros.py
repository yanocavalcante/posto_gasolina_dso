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
                
                id_para_alterar = self.verifica_id_alterar(id_para_alterar)

                pessoa = self.verifica_existencia_id_alterar(id_para_alterar)
                
                if pessoa == None:
                    self.input_opcao_cadastros()

                info_pessoa = {}

                info_pessoa['nome'], info_pessoa['idade'], info_pessoa['cpf'], info_pessoa['telefone'] = self.__tela_cadastros.opcao_alterar()
                
                info_pessoa = self.verifica_idade(info_pessoa)
                info_pessoa = self.verifica_cpf(info_pessoa)
                info_pessoa = self.verifica_telefone(info_pessoa)

                pessoa.nome = info_pessoa['nome'] if info_pessoa['nome'] is not None else pessoa.nome
                pessoa.idade = info_pessoa['idade'] if info_pessoa['idade'] is not None else pessoa.idade
                pessoa.cpf = info_pessoa['cpf'] if info_pessoa['cpf'] is not None else pessoa.cpf
                pessoa.telefone = info_pessoa['telefone'] if info_pessoa['telefone'] is not None else pessoa.telefone

                self.input_opcao_cadastros()

            elif opcao_pessoa == 3:
                
                print("-"*20)
                self.mostra_lista_pessoas()
                print("-"*20)
                print('EXCLUIR PESSOA')

                id_para_excluir = self.__tela_cadastros.input_id_para_excluir()

                id_para_excluir = self.verifica_id_excluir(id_para_excluir)

                pessoa = self.verifica_existencia_id_excluir(id_para_excluir)
                
                self.excluir_pessoa(pessoa)

                self.input_opcao_cadastros()

            elif opcao_pessoa == 4:
                self.mostra_lista_pessoas()
                
                input("Digite qualquer coisa para voltar: ")

                self.input_opcao_cadastros()

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
        
    def verifica_existencia_id_alterar(self, id):
        if self.lista_pessoas == []:
            print("Não existe nenhuma pessoa na lista!")
            return
        
        id = self.verifica_id_alterar(id)
        for pessoa in self.lista_pessoas:
            
            if pessoa.id == id:
                
                return pessoa
            
        id_para_alterar = self.__tela_cadastros.input_id_para_alterar()
        return self.verifica_existencia_id_alterar(id_para_alterar)
        
    
    def mostra_lista_pessoas(self):
        for pessoa in self.lista_pessoas:
            self.tela_pessoa.mostra_pessoa(pessoa)

    def verifica_id_alterar(self, id):
        try:
            id = int(id)
            return id
        except ValueError:
            id = self.__tela_cadastros.input_id_para_alterar()
            self.verifica_id_alterar(id)

    def excluir_pessoa(self, pessoa_para_excluir):
        for index, pessoa in enumerate(self.lista_pessoas):
            
            if pessoa_para_excluir.id == pessoa.id:
                self.lista_pessoas.pop(index)

    def verifica_id_excluir(self, id):
        try:
            id = int(id)
            return id
        except ValueError:
            id = self.__tela_cadastros.input_id_para_excluir()
            self.verifica_id_excluir(id)

    def verifica_existencia_id_excluir(self, id):
        if self.lista_pessoas == []:
            print("Não existe nenhuma pessoa na lista!")
            return
        
        id = self.verifica_id_excluir(id)
        for pessoa in self.lista_pessoas:
            
            if pessoa.id == id:
                
                return pessoa
            
        id_para_excluir = self.__tela_cadastros.input_id_para_excluir()
        return self.verifica_existencia_id_excluir(id_para_excluir)