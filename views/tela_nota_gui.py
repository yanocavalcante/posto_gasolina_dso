import PySimpleGUI as sg


class TelaNotas():
    def __init__(self):
        self.__window = None
        self.input_tipo_nota()

    def input_tipo_nota(self):
        sg.theme('DarkAmber')
        layout = [
                  [sg.Text('Notas', font = ('Helvica', 25))],
                  [sg.Text('Opções:', font = ('Helvica', 15))],
                  [sg.Radio('Saída', 'G2', key = '1')],
                  [sg.Radio('Entrada', 'G2', key = '2')],
                  [sg.B('Confirmar'), sg.B('Voltar')]
        ]
        self.__window = sg.Window('Menu - Notas').Layout(layout)

    def open(self):
        event, values = self.__window.Read()
        return event, values
        # if values['1']:
        #     op = 1
        # elif values['2']:
        #     op = 2
        # if event in [None, 'Voltar']:
        #     op = 3
        # self.close()
        # return op
    
    def input_produtos(self):
        sg.theme('DarkAmber')
        layout = [
                  [sg.Text('------PRODUTOS------', font = ('Helvica',25))]
                  [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
                  [sg.Text('Quantidade:'), sg.Input('', key = ('qnt'))],
                  [sg.Text('Adicionar + Produtos')],
                  [sg.Radio('Sim', 'G3', key='1'), sg.Radio('Não', 'G3', key = '0')]
        ]
        self.__window = sg.Window('Sistema').Layout(layout)
        event, values = self.open()
        print(values)
        nome = values['nome']
        qnt = values['qnt']
        if values['1']:
            op = True
        elif values['0']:
            op = False
        self.close()
        return {'nome': nome, 'qnt': qnt, 'op': op}


    def close(self):
        self.__window.Close()
