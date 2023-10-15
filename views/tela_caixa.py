class TelaCaixa:
    def seleciona_caixa(self):
        print('CAIXAS')
        caixa = input('Caixa:')
        return caixa
    
    def seleciona_acao(self):
        print('CAIXAS')
        print('1 - Cadastrar    2 - Consultar       3 - Voltar')
        op = int(input())
        return op
    
    def input_info_caixa(self):
        print('CAIXAS')
        print('Tipos')
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