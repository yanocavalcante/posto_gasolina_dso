from views.tela_principal import TelaPrincipal

class TelaNotas(TelaPrincipal):

    def mostra_tipo_notas(self):
        self.limparTela()
        self.cabecalho('Notas')
        print('1 - Saída        2 - Entrada        3 - Retornar')
        op = self.le_opcoes([1,2,3])
        return op

    def listagem_produtos(self):
        produtos = []
        self.subcabecalho('PRODUTOS')
        while True:
            nome = input('Nome:')
            qnt = int(input('Quantidade:'))
            produto = {'nome': nome, 'qnt': qnt}
            produtos.append(produto)
            print('1 - Adicionar Produto        2 - Finalizar')
            act = self.le_opcoes([1,2])
            if act == 2:
                break
        return produtos

    def input_notaSaida(self):
        self.subcabecalho('NOTA DE SAÍDA')
        cliente = input('Cliente:')
        self.subcabecalho('')
        produtos = self.listagem_produtos()
        return cliente, produtos

    def input_notaEntrada(self):
        self.subcabecalho('NOTA DE ENTRADA')
        fornecedor = input('Fornecedor:')
        produtos = self.listagem_produtos()
        return fornecedor, produtos
        