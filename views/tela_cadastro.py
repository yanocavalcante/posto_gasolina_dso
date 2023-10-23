from views.tela_principal import TelaPrincipal, sleep


class TelaCadastros(TelaPrincipal):

    def mostra_opcoes(self,):
        self.limparTela()
        self.cabecalho('Cadastros')
        self.subcabecalho('Tipos')
        print("1 - Produtos       2 - Pessoas       3 - Voltar")
        op = self.le_opcoes([1,2,3,])
        return op
    
    def input_id_para_alterar(self):
        id_para_alterar = input("Digite o id para alterar: ")
        return id_para_alterar
    
    def opcao_alterar(self):
        nome = input("Novo nome: ")
        cpf = input("Novo cpf: ")
        telefone = input("Novo telefone: ")
        idade = input("Nova idade: ")

        return nome, idade, cpf, telefone
    
    def input_id_para_excluir(self):
        id_para_excluir = input("Digite o id da pessoa que deseja excluir: ")
        return id_para_excluir
