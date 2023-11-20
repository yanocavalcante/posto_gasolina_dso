import PySimpleGUI as sg


class TelaNotas():
    def __init__(self):
        self.__window = None
        self.init_tipo_nota()

    def mostra_mensagem(self, msg):
        sg.theme('DarkAmber')
        sg.Popup(f'{msg}')

    def tela_tipo_nota(self):
        self.init_tipo_nota()
        event, values = self.open()
        if values['1']:
            op = 1
        if values['2']:
            op = 2
        if event in (None, 'Voltar'):
            op = 3
        self.close()
        return op

    def init_tipo_nota(self):
        sg.theme('DarkAmber')
        layout = [
                  [sg.Text('Notas', font = ('Helvica', 25))],
                  [sg.Text('Selecione o tipo de Nota:', font = ('Helvica', 15))],
                  [sg.Radio('Saída', 'G2', key = '1')],
                  [sg.Radio('Entrada', 'G2', key = '2')],
                  [sg.B('Confirmar'), sg.B('Voltar')]
        ]
        self.__window = sg.Window('Menu Notas').Layout(layout)

    def input_produtos(self):
        sg.theme('DarkAmber')
        layout = [
                  [sg.Text('Listagem de Produtos', font = ('Helvica',25))],
                  [sg.Text('Nome:'), sg.InputText('', key='nome')],
                  [sg.Text('Quantidade:'), sg.Input('', key = 'qnt', enable_events=True)],
                  [sg.Text('Deseja Adicionar Mais Produtos?')],
                  [sg.Radio('Sim', 'G3', key='1'), sg.Radio('Não', 'G3', key = '0')],
                  [sg.B('Confirmar')]
        ]
        self.__window = sg.Window('Sistema').Layout(layout)
        while True:
            event, values = self.open()
            if event == 'Confirmar':
                try:
                    qnt = int(values['qnt'])
                    break
                except ValueError:
                    self.mostra_mensagem('Valor Inválido para "Quantidade"!')
        nome = values['nome']
        if values['1']:
            op = True
        elif values['0']:
            op = False
        self.close()
        return {'nome': nome, 'qnt': qnt, 'op': op}

    def open(self):
        event, values = self.__window.Read()
        return event, values

    def close(self):
        self.__window.Close()
