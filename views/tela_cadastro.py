from views.tela_principal import TelaPrincipal

class TelaCadastros:
    def __init__(self) -> None:
        pass

    def mostra_opcoes(self,):
        print("-"*20)
        print("1 - Cadastro de Produtos")
        print("2 - Cadastro de Pessoas")
        print("3 - Voltar ao início")
        opcao = input("Digite uma opção: ")
        try:
            opcao = int(opcao)
        except ValueError:
            print("-"*20)
            print("Digite um número válido!")
            print("-"*20)

        while opcao not in [1, 2, 3]:
            print("1 - Cadastro de Produtos")
            print("2 - Cadastro de Pessoas")
            print("3 - Voltar ao início")
            opcao = input("Digite uma opção: ")
            try:
                opcao = int(opcao)
            except ValueError:
                print("-"*20)
                print("Digite um número válido!")
                print("-"*20)

        return opcao
    
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
