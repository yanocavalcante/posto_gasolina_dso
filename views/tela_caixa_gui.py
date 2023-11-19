import PySimpleGUI as sg


class TelaCaixa():
    def __init__(self):
        self.__window = None

    def mostra_mensagem(self, msg):
        sg.theme('DarkAmber')
        sg.Popup(f'{msg}')

    def tela_acao(self):
        self.seleciona_acao()
        event, values = self.open()
        if event in [None, 'Voltar']:
            op = 3        
        elif values['1']:
            op = 1
        elif values['2']:
            op = 2
        self.close()
        return op

    def input_cadastro_caixa(self):
        sg.theme('DarkAmber')
        layout = [
                  [sg.Text('Caixas', font = ('Helvica', 25))],
                  [sg.Text('Nome:'), sg.In('', key = 'nome')],
                  [sg.Text('Saldo Inicial:'), sg.In('', key = 'saldo')],
                  [sg.Text('Crédito:'), sg.In('', key = 'credito')],
                  [sg.Radio('Físico', 'G4', key = 'fisico'), sg.Radio('Bancário', 'G4', key = 'bancario')]
        ]
        self.__window = sg.Window('Sistema').Layout(layout)

    def input_caixa(self):
        sg.theme('DarkAmber')
        layout = [
                  [sg.Text('Caixas', font = ('Helvica', 25))],
                  [sg.Text('Nome:'), sg.In('', key = 'nome')],
                  [sg.B('Confirmar')]
        ]
        self.__window = sg.Window('Sistema').Layout(layout)

    def seleciona_acao(self):
        sg.theme('DarkAmber')
        layout = [
                  [sg.Text('Opções:')],
                  [sg.Radio('Cadastrar', 'G5', key = '1')],
                  [sg.Radio('Consultar', 'G5', key = '2')],
                  [sg.B('Confirmar'), sg.B('Voltar')]
        ]
        self.__window = sg.Window('Sistema').Layout(layout)

    def open(self):
        event, values = self.__window.Read()
        return event, values

    def close(self):
        self.__window.Close()
