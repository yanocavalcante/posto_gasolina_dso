import PySimpleGUI as sg


class TelaCaixa():
    def __init__(self):
        self.__window = None

#POPUPS
    def caixa_n_encontrado(self):
        sg.theme('DarkAmber')
        sg.Popup('Caixa Não Encontrado!')

    def cancela_operacao(self):
        sg.theme('DarkAmber')
        sg.Popup('Por Conta de Insuficiência no Saldo a Operação foi cancelada!')

    def uso_credito(self, credito_restante):
        sg.theme('DarkAmber')
        sg.Popup(f'AVISO: Para essa operação parte do crédito foi utilizada, restante: {credito_restante}')

    def tela_acao(self):
        self.seleciona_acao()
        event, values = self.open()
        if event in [None, 'Voltar']:
            op = 3        
        elif values['1']:
            op = 1
        elif values['2']:
            op = 2
        return op

#LAYOUTS
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

#MÉTODOS BASE
    def open(self):
        event, values = self.__window.Read()
        return event, values

    def close(self):
        self.__window.Close()
