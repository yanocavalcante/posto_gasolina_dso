import PySimpleGUI as sg


class TelaNotas():
    def __init__(self):
        self.__window = None
        self.init_tipo_nota()

    def mostra_mensagem(self, msg):
        sg.theme('DarkAmber')
        sg.Popup(f'{msg}', font=('Verdana',12))

    def tela_tipo_nota(self):
        self.init_tipo_nota()
        event, values = self.open()
        if event == 'Saída':
            op = 1
        if event == 'Entrada':
            op = 2
        if event in (None, 'Voltar'):
            op = 3
        self.close()
        return op

    def init_tipo_nota(self):
        sg.theme('DarkAmber')
        layout = [
                  [sg.Text('----Notas----', font = ('Helvica', 25))],
                  [sg.Text('', size=(15, 1))],
                  [sg.Button('Saída', font = ('Verdana', 12), size=(18))],
                  [sg.Button('Entrada', font=('Verdana', 12), size=(18))],
                  [sg.T('')],
                  [sg.B('Voltar', font=('Verdana', 8))]
        ]
        self.__window = sg.Window('Menu Notas').Layout(layout)

    def input_produtos(self):
        sg.theme('DarkAmber')
        layout = [
                  [sg.Text('Listagem de Produtos', font = ('Verdana',25))],
                  [sg.Text('Nome:', size=(12, 1), font=('Verdana', 12)), sg.InputText('', key='nome', size=(25, 1))],
                  [sg.Text('Quantidade:', size=(12, 1), font=('Verdana', 12)),
                    sg.Input('', key = 'qnt', enable_events=True, size=(25, 1))],
                  [sg.T('')],
                  [sg.Text('Deseja Adicionar Mais Produtos?', font=('Verdana', 12))],
                  [sg.Radio('Sim', 'G3', key= '1', font=('Verdana', 12)),
                   sg.Radio('Não', 'G3', key = '0', font=('Verdana',12))],
                  [sg.T('')],
                  [sg.B('Confirmar', font=('Verdana', 9))]
        ]
        self.__window = sg.Window('Menu Notas').Layout(layout)
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
