

class TelaPessoa:
    def __init__(self) -> None:
        pass

    def mostra_opcoes(self,) -> int:
        print("1 - Cadastrar Pessoa")
        print("2 - Alterar Pessoa")
        print("3 - Excluir Pessoa")
        opcao = input("Digite a opção desejada: ")

        while opcao not in [1, 2, 3]:
            print("1 - Cadastrar Pessoa")
            print("2 - Alterar Pessoa")
            print("3 - Excluir Pessoa")
            opcao = input("Digite a opção desejada: ")

        return opcao