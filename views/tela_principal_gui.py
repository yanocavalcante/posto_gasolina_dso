import PySimpleGUI as sg


class TelaPrincipal():
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('Software Ypê', font = ('Helvica', 25))],
            [sg.Text('Seja Bem-Vindo!',
                     font= ('Helvica', 10))],
            [sg.Text('Menu Inicial:', font = ('Helvica', 20))],
            [sg.Radio('Cadastros', 'G1', key = '1')],
            [sg.Radio('Caixas', 'G1', key = '2')],
            [sg.Radio('Notas', 'G1', key = '3')],
            [sg.B('Confirmar'), sg.Exit('Sair')]
        ]
        self.__window = sg.Window('Menu Inicial').Layout(layout)

    def open(self):
        self.init_components()
        event, values = self.__window.Read()
        if event in [None]:
            op = 4
        elif values['1']:
            op = 1
        elif values['2']:
            op = 2
        elif values['3']:
            op = 3
        self.close()
        return op

    def close(self):
        self.__window.Close()