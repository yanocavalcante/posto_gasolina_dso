

class TelaPessoa:
    def __init__(self) -> None:
        pass

    def mostra_opcoes_pessoa(self,) -> int:
        print("-"*20)
        print("1 - Cadastrar Pessoa")
        print("2 - Alterar Pessoa")
        print("3 - Excluir Pessoa")
        print("4 - Listar Pessoas")
        opcao = input("Digite a opção desejada: ")

        try:
            opcao = int(opcao)

            if opcao not in [1, 2, 3, 4]:
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
        funcionario = input("Ele é um funcionário do posto? (S/N): ").upper()
        
        return {"nome": nome, "idade": idade, "cpf": cpf, "telefone": telefone, "funcionario": funcionario}

    def input_idade(self):
        idade = input("Digite a idade da pessoa: ")
        
        return idade
    
    def input_funcionario(self):
        funcionario = input("Ele é um funcionário do posto? (S/N): ").upper()
        
        return funcionario

    def mostra_pessoa(self, dados_pessoa):
        print(f"Nome da pessoa: {dados_pessoa.nome}")
        print(f"Id da pessoa: {dados_pessoa.id}")
        print("\n")