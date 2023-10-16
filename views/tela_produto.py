
class TelaProduto:
    def __init__(self) -> None:
        pass

    def opcoes_produto(self):
        print("-"*20)
        print("1 - Cadastrar Produto")
        print("2 - Alterar Produto")
        print("3 - Excluir Produto")
        print("4 - Listar Produtos")
        print("5 - Voltar")
        opcao = input("Digite a opção desejada: ")

        try:
            opcao = int(opcao)
        except ValueError:
            print("-"*20)
            print("Digite um número válido!")
            print("-"*20)

        while opcao not in [1, 2, 3, 4, 5]:
            print("-"*20)
            print("1 - Cadastrar Produto")
            print("2 - Alterar Produto")
            print("3 - Excluir Produto")
            print("4 - Listar Produtos")
            print("5 - Voltar")
            opcao = input("Digite uma opção: ")
            try:
                opcao = int(opcao)
            except ValueError:
                print("-"*20)
                print("Digite um número válido!")
                print("-"*20)

        return opcao


    def input_info_produto(self):
        print("-"*20)
        print("CADASTRO DE PRODUTOS")
        categoria = input("Digite a categoria do produto: ")
        nome = input("Digite o nome do produto: ")
        fornecedor = input("Digite o nome do fornecedor: ")
        custo = input("Digite o custo do produto: ")
        preco = input("Digite o preco do produto: ")
        estoque = input("Digite a quantidade no estoque: ")

        return {'categoria': categoria, 'nome': nome, 'fornecedor': fornecedor, 'custo': custo, 'preco': preco, 'estoque': estoque}
    
    def mostra_produto(self, dados_produto):
        print(f"Nome do produto: {dados_produto.nome}")
        print(f"Id do produto: {dados_produto.id}")
        print(f"Categoria do produto: {dados_produto.categoria}")
        print(f"Custo do produto: {dados_produto.custo}")
        print(f"Preco do produto: {dados_produto.preco}")
        print(f"Estoque: {dados_produto.estoque}")
        print("\n")

    def input_id_para_alterar(self):
        id_para_alterar = input("Digite o id para alterar: ")
        return id_para_alterar
    
    def alterar_info_produto(self):
        nome = input("Novo nome: ")
        categoria = input("Nova categoria: ")
        fornecedor = input("Novo fornecedor: ")
        custo = input("Novo custo: ")
        preco = input("Nova preco: ")

        return nome, categoria, fornecedor, custo, preco
    
    def input_id_para_excluir_produto(self):
        id_para_excluir = input("Digite o id do produto que deseja excluir: ")
        return id_para_excluir