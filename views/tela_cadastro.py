

class TelaCadastros:
    def __init__(self) -> None:
        pass

    def mostra_opcoes(self,):
        print("-"*20)
        print("1 - Cadastro de Produtos")
        print("2 - Cadastro de Pessoas")
        opcao = input("Digite uma opção: ")
        try:
            opcao = int(opcao)
        except ValueError:
            print("-"*20)
            print("Digite um número válido!")
            print("-"*20)

        while opcao not in [1, 2]:
            print("1 - Cadastro de Produtos")
            print("2 - Cadastro de Pessoas")
            opcao = input("Digite uma opção: ")
            try:
                opcao = int(opcao)
            except ValueError:
                print("-"*20)
                print("Digite um número válido!")
                print("-"*20)

        return opcao