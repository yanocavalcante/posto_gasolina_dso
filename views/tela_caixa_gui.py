import PySimpleGUI as sg


class TelaCaixa():
    def __init__(self):
        self.__window = None
        self.init_acao()

    def mostra_mensagem(self, msg):
        sg.theme('DarkAmber')
        sg.Popup(f'{msg}', font=('Verdana', 12))

    def tela_acao(self):
        self.init_acao()
        event, values = self.open()
        if event in (None, 'Voltar'):
            op = 3        
        elif event == 'Cadastrar':
            op = 1
        elif event == 'Consultar':
            op = 2
        self.close()
        return op

    def input_cadastro_caixa(self):
        sg.theme('DarkAmber')
        layout = [
                  [sg.Text('---Caixas---', font = ('Verdana', 25))],
                  [sg.Text('Novo Caixa', font= ('Verdana', 18))],
                  [sg.Text('Nome:', size=(10,1), font=('Verdana', 12)),
                    sg.In('', key = 'nome', size=(25, 1))],
                  [sg.Text('Saldo Inicial:', size=(10,1), font=('Verdana', 12)),
                    sg.In('', key = 'saldo', enable_events=True, size=(25, 1))],
                  [sg.Text('Crédito:', size=(10,1), font=('Verdana', 12)),
                    sg.In('0', key = 'credito', enable_events=True, size=(25, 1))],
                  [sg.Radio('Físico', 'G4', key = 'fisico', font=('Verdana', 12)),
                    sg.Radio('Bancário', 'G4', key = 'bancario', font=('Verdana', 12))],
                  [sg.T('')],
                  [sg.B('Confirmar', font=('Verdana', 9))]
        ]
        self.__window = sg.Window('Menu Caixas').Layout(layout)
        while True:
            event, values = self.open()
            if event == 'Confirmar':
                try:
                    saldo = int(values['saldo'])
                    credito = int(values['credito'])
                    break
                except ValueError:
                    self.mostra_mensagem('Valor Inválido para "Saldo" e/ou "Crédito"!')
        nome = values['nome']
        if values['fisico']:
            tipo = 'Físico'
            credito = 0
        else:
            tipo = 'Bancário'
        self.close()
        return tipo, nome, saldo, credito

    def input_caixa(self, lista_caixas= []):
        sg.theme('DarkAmber')
        layout = [
                  [sg.Text('---Caixas---', font = ('Verdana', 25))],
                  [sg.Text('Selecione um Caixa:', font= ('Verdana', 18))],
                  [sg.Text('Nome:', font=('Verdana', 12)), sg.InputCombo(lista_caixas, key = 'nome')],
                  [sg.T('')],
                  [sg.B('Confirmar', font=('Verdana', 9))]
        ]
        self.__window = sg.Window('Menu Caixas').Layout(layout)
        event, values = self.open()
        nome = values['nome']
        self.close()
        return nome
    
    def imprime_historico(self, movimentos, saldo_inicial, saldo, credito=0):
        layout = [
        [sg.T('Histórico de Movimentações')],
        [sg.T(f'Saldo Inicial: R$ {saldo_inicial:.2f}')],
        [sg.T(f'Crédito: {credito}')],
        [sg.Table(values=list(movimentos.items()),
                  headings=['N° da Nota', 'Valor da Nota'],
                  auto_size_columns=False,
                  justification='right',
                  num_rows=min(25, len(movimentos)),
                  col_widths=[10, 10])],
        [sg.T(f'Saldo Final: R$ {saldo:.2f}')],
        [sg.Button('Fechar')]
        ]
        self.__window = sg.Window('Histórico Caixas').Layout(layout)
        while True:
            event, values = self.open()
            if event == sg.WIN_CLOSED or event == 'Fechar':
                break
        self.close()

    def init_acao(self):
        sg.theme('DarkAmber')
        layout = [
                  [sg.Text('---Caixas---', font = ('Verdana', 25))],
                  [sg.Text('')],
                  [sg.B('Cadastrar', font = ('Verdana', 12), size=(18))],
                  [sg.B('Consultar', font = ('Verdana', 12), size=(18))],
                  [sg.T('')],
                  [sg.B('Voltar', font=('Verdana', 9))]
        ]
        self.__window = sg.Window('Menu Caixas').Layout(layout)

    def open(self):
        event, values = self.__window.Read()
        return event, values

    def close(self):
        self.__window.Close()
