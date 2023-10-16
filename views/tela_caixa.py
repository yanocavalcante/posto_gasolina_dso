from views.tela_principal import TelaPrincipal


class TelaCaixa(TelaPrincipal):

    def seleciona_caixa(self):
        self.limparTela()
        self.cabecalho('Caixas')
        caixa = input('Caixa:')
        return caixa
    
    def seleciona_acao(self):
        self.limparTela()
        self.cabecalho('Caixas')
        print('1 - Cadastrar    2 - Consultar       3 - Voltar')
        op = int(input())
        return op
    
    def input_info_caixa(self):
        self.limparTela()
        self.cabecalho('Caixas')
        self.subcabecalho('Tipos')
        print('1 - Físico       2 - Bancário')
        tipo = input()
        nome = input('Nome:')
        saldo = float(input('Saldo Inicial:'))
        if tipo == '2':
            tipo = 'Bancário'
            credito = 'Crédito:'
        else:
            tipo = 'Físico'
            credito = None
        return tipo, nome, saldo, credito