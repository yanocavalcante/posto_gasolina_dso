from views.tela_principal import TelaPrincipal, sleep

class TelaNotas(TelaPrincipal):

    def mostra_tipo_notas(self):
        self.limparTela()
        self.cabecalho('Notas')
        print('1 - Saída        2 - Entrada        3 - Voltar')
        op = self.le_opcoes([1,2,3])
        return op
    
    def le_opcoes(self, ops):
        try:
            op = int(input())
            if op in ops:
                return op
            else:
                raise Exception
        except Exception:
            print('Valor Inválido. Reinicie a Listagem.')
            sleep(2)
            self.listagem_produto()

    def listagem_produto(self):
        nome = input('Nome:')
        qnt = int(input('Quantidade:'))
        print('1 - Adicionar Produto        2 - Finalizar')
        op = self.le_opcoes([1,2])
        if op == 1:
            op = True
        else:
            op = False
        return nome, qnt, op

    def input_notaSaida(self):
        self.subcabecalho('NOTA DE SAÍDA')
        self.subcabecalho('Produtos')
        nome, qnt, op = self.listagem_produto()
        return nome, qnt, op

    def input_notaEntrada(self):
        self.subcabecalho('NOTA DE ENTRADA')
        self.subcabecalho('Produtos')
        nome, qnt, op = self.listagem_produto()
        return nome, qnt, op
    
    def input_cliente(self):
        cliente = str(input('Cliente:'))
        return cliente
    
    def input_fornecedor(self):
        fornecedor = str(input('Fornecedor:'))
        return fornecedor 