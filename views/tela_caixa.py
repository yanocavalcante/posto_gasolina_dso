from views.tela_principal import TelaPrincipal, sleep


class TelaCaixa(TelaPrincipal):

    def seleciona_caixa(self):
        self.limparTela()
        self.cabecalho('Caixas')
        caixa = str(input('Caixa:'))
        return caixa
    
    def seleciona_acao(self):
        self.limparTela()
        self.cabecalho('Caixas')
        print('1 - Cadastrar        2 - Consultar        3 - Voltar')
        op = self.le_opcoes([1,2,3])
        return op
    
    def input_info_caixa(self):
        self.limparTela()
        self.cabecalho('Caixas')
        self.subcabecalho('Tipos')
        print('1 - Físico       2 - Bancário')
        tipo = self.le_opcoes([1,2])
        nome = input('Nome:')
        saldo = float(input('Saldo Inicial:'))
        if tipo == 2:
            tipo = 'Bancário'
            credito = 'Crédito:'
        else:
            tipo = 'Físico'
            credito = None
        return tipo, nome, saldo, credito
    
    def imprime_historico(self, listamovimentos, caixa):
        self.cabecalho(f'Histórico - {caixa.nome}')
        for nota in listamovimentos:
            print(nota.num, '-', nota.valor)
        print(caixa.saldo)
        sleep(5)
