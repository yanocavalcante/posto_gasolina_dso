from views.tela_cadastro import TelaCadastros
from views.tela_pessoa import TelaPessoa
from models.cliente import Cliente
from models.funcionario import Funcionario
from views.tela_produto import TelaProduto
from models.produto import Produto
class CtrlCadastros:
    def __init__(self, controlador_principal) -> None:
        self.__lista_pessoas = []
        self.__lista_produtos = []
        self.__tela_pessoa = TelaPessoa()
        self.__tela_produto = TelaProduto()
        self.__tela_cadastros = TelaCadastros()
        self.__controlador_principal = controlador_principal

    @property
    def lista_pessoas(self):
        return self.__lista_pessoas
    
    @property
    def lista_produtos(self):
        return self.__lista_produtos

    @property
    def tela_pessoa(self):
        return self.__tela_pessoa
    
    @property
    def tela_produto(self):
        return self.__tela_produto
    
    def input_opcao_cadastros(self):
        
        opcao = self.__tela_cadastros.mostra_opcoes()
        
        if opcao == 1:
            opcao_produto = self.tela_produto.opcoes_produto()

            if opcao_produto == 1:
                
                info_produto = self.tela_produto.input_info_produto()

                info_produto = self.verifica_custo(info_produto)
                info_produto = self.verifica_preco(info_produto)
                info_produto = self.verifica_valor_estoque(info_produto)

                self.lista_produtos.append(Produto(id=0 if self.lista_produtos == [] else self.lista_produtos[-1].id + 1,
                                                   categoria=info_produto['categoria'],
                                                   nome=info_produto['nome'],
                                                   fornecedor=info_produto['fornecedor'],
                                                   custo=info_produto['custo'],
                                                   preco=info_produto['preco'],
                                                   estoque=info_produto['estoque']))
                
                self.input_opcao_cadastros()
                
            elif opcao_produto == 2:
                self.mostra_lista_produtos()

                id_para_alterar_produto = self.tela_produto.input_id_para_alterar()

                id_para_alterar_produto = self.verifica_id_alterar_produto(id_para_alterar_produto)

                produto = self.verifica_existencia_id_alterar_produto(id_para_alterar_produto)

                if produto == None:
                    self.input_opcao_cadastros()

                info_produto = {}

                info_produto['nome'], info_produto['categoria'], info_produto['fornecedor'], info_produto['custo'], info_produto['preco'] = self.tela_produto.alterar_info_produto()
                
                info_produto = self.verifica_custo(info_produto)
                info_produto = self.verifica_preco(info_produto)
                

                produto.nome = info_produto['nome'] if info_produto['nome'] is not None else produto.nome
                produto.categoria = info_produto['categoria'] if info_produto['categoria'] is not None else produto.categoria
                produto.fornecedor = info_produto['fornecedor'] if info_produto['fornecedor'] is not None else produto.fornecedor
                produto.custo = info_produto['custo'] if info_produto['custo'] is not None else produto.custo
                produto.preco = info_produto['preco'] if info_produto['preco'] is not None else produto.preco

                self.input_opcao_cadastros()

            elif opcao_produto == 3:
                print("-"*20)
                self.mostra_lista_produtos()
                print("-"*20)
                print('EXCLUIR PRODUTO')

                id_para_excluir = self.tela_produto.input_id_para_excluir_produto()

                id_para_excluir = self.verifica_id_excluir_produto(id_para_excluir)

                produto = self.verifica_existencia_id_excluir_produto(id_para_excluir)
                
                self.excluir_produto(produto)

                self.input_opcao_cadastros()

            elif opcao_produto == 4:
                self.mostra_lista_produtos()

                input("Digite qualquer coisa para voltar: ")

                self.input_opcao_cadastros()
            
            elif opcao_produto == 5:
                self.voltar()

        elif opcao == 2:
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
            
            elif opcao_pessoa == 5:
                self.voltar()

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
    
    def verifica_existencia_id_alterar_produto(self, id):
        if self.lista_produtos == []:
            print("Não existe nenhum produto na lista!")
            return
        
        id = self.verifica_id_alterar(id)
        for produto in self.lista_produtos:
            
            if produto.id == id:
                
                return produto
            
        id_para_alterar = self.tela_produto.input_id_para_alterar()
        return self.verifica_existencia_id_alterar_produto(id_para_alterar)
        
    
    def mostra_lista_pessoas(self):
        print("-"*20)
        for pessoa in self.lista_pessoas:
            self.tela_pessoa.mostra_pessoa(pessoa)

    def verifica_id_alterar(self, id):
        try:
            id = int(id)
            return id
        except ValueError:
            id = self.__tela_cadastros.input_id_para_alterar()
            return self.verifica_id_alterar(id)

    def verifica_id_alterar_produto(self, id):
        try:
            id = int(id)
            return id
        except ValueError:
            id = self.tela_produto.input_id_para_alterar()
            return self.verifica_id_alterar_produto(id)

    def excluir_pessoa(self, pessoa_para_excluir):
        for index, pessoa in enumerate(self.lista_pessoas):
            
            if pessoa_para_excluir.id == pessoa.id:
                self.lista_pessoas.pop(index)
    
    def excluir_produto(self, produto_para_excluir):
        for index, produto in enumerate(self.lista_produtos):
            
            if produto_para_excluir.id == produto.id:
                self.lista_produtos.pop(index)

    def verifica_id_excluir(self, id):
        try:
            id = int(id)
            return id
        except ValueError:
            id = self.__tela_cadastros.input_id_para_excluir()
            return self.verifica_id_excluir(id)

    def verifica_id_excluir_produto(self, id):
        try:
            id = int(id)
            return id
        except ValueError:
            id = self.tela_produto.input_id_para_excluir_produto()
            return self.verifica_id_excluir(id)

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
    
    def verifica_existencia_id_excluir_produto(self, id):
        if self.lista_produtos == []:
            print("Não existe nenhum produto na lista!")
            return
        
        id = self.verifica_id_excluir_produto(id)
        for produto in self.lista_produtos:
            
            if produto.id == id:
                
                return produto
            
        id_para_excluir = self.tela_produto.input_id_para_excluir_produto()
        return self.verifica_existencia_id_excluir_produto(id_para_excluir)

    def verifica_custo(self, info_produto):
        try:
            info_produto['custo'] = float(info_produto['custo'])
            return info_produto
        except ValueError:
            info_produto['custo'] = input('Digite um custo válido: ')
            return self.verifica_custo(info_produto)
        

    def verifica_preco(self, info_produto):
        try:
            info_produto['preco'] = float(info_produto['preco'])
            return info_produto
        except ValueError:
            info_produto['preco'] = input('Digite um preço válido: ')
            return self.verifica_preco(info_produto)
        
    def verifica_valor_estoque(self, info_produto):
        try:
            info_produto['estoque'] = int(info_produto['estoque'])
            return info_produto
        except ValueError:
            info_produto['estoque'] = input('Digite um valor válido para o estoque: ')
            return self.verifica_valor_estoque(info_produto)
        
    def mostra_lista_produtos(self):
        print("-"*20)
        for produto in self.lista_produtos:
            self.tela_produto.mostra_produto(produto)

    
    def voltar(self):
        self.input_opcao_cadastros()

    def verifica_lista_clientes(self, cliente):
        for clientes in self.lista_pessoas:
            if clientes.nome == cliente.nome:
                return clientes

    def verifica_lista_produtos(self, produto):
        for produtos in self.lista_produtos:
            if produtos.nome == produto.nome:
                return produtos
            
    def diminuir_estoque(self, valor_diminuir, produto):
        if valor_diminuir > produto.estoque:
            print("Impossível realizar essa operação! Valor maior que o estoque do produto!")
            return 
        else:
            produto.estoque -= valor_diminuir

    def aumentar_estoque(self, valor_aumentar, produto):
        for prod in self.lista_produtos:
            if prod.nome == produto:
                prod.estoque += valor_aumentar