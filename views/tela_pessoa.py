

class TelaPessoa:
    def __init__(self) -> None:
        pass

    def mostra_opcoes_pessoa(self,) -> int:
        print("-"*20)
        print("1 - Cadastrar Pessoa")
        print("2 - Alterar Pessoa")
        print("3 - Excluir Pessoa")
        opcao = input("Digite a opção desejada: ")

        try:
            opcao = int(opcao)

            if opcao not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            return self.mostra_opcoes_pessoa()


        return opcao
    

    def input_cadastro_pessoa(self) -> dict:
        print("-"*20)
        print("CADASTRO DE PESSOA")
        nome = input("Digite o nome da pessoa: ")
        idade = input("Digite a idade da pessoa: ")
        cpf = input("Digite o cpf da pessoa: ")
        telefone = input("Digite o telefone da pessoa: ")
        funcionario = input("Ele é um funcionário do posto? (S/N): ")
        
        return {"nome": nome, "idade": idade, "cpf": cpf, "telefone": telefone, "funcionario": funcionario}