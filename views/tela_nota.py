class TelaNotas:

    def mostra_tipo_notas(self):
        print('NOTAS')
        print('1 - Saída        2 - Entrada')
        op = input()
        return op

    def input_notaSaida(self):
        print('NOTA DE SAÍDA')
        cliente = input('Cliente')
        caixa = input('Caixa:')
        print('PRODUTOS')
        produtos = []
        while True:
            nome = input('Nome:')
            qnt = input('Quantidade:')
            produto = {'nome': nome, 'qnt': qnt}
            produtos.append(produto)
        return cliente, caixa, produtos

    def input_notaEntrada(self):
        print('NOTA DE ENTRADA')
        fornecedor = input('Fornecedor:')
        caixa = input('Caixa:')
        print('PRODUTOS')
        produtos = []
        while True:
            nome = input('Nome:')
            qnt = input('Quantidade:')
            produto = {'nome': nome, 'qnt': qnt}
            produtos.append(produto)
        return fornecedor, caixa, produtos