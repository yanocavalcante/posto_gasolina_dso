import PySimpleGUI as sg


class TelaPrincipal():
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('S10 Software Inc.', font=('Helvetica', 25))],
            [sg.Text('---Menu Inicial---', font=('Helvetica', 20))],
            [sg.Button('Cadastros', size=(12, 2)), 
            sg.Button('Caixas', size=(12, 2)), 
            sg.Button('Notas', size=(12, 2))],
            [sg.Button('Confirmar', size=(10, 1)), 
            sg.Exit('Sair', size=(10, 1))]
        ]
        self.__window = sg.Window('Menu Inicial').Layout(layout)

    def open(self):
        self.init_components()
        event, values = self.__window.Read()
        if event in [None, 'Sair']:
            op = 4
        elif event == 'Cadastros':
            op = 1
        elif event == 'Caixas':
            op = 2
        elif event == 'Notas':
            op = 3
        self.close()
        return op

    def close(self):
        self.__window.Close()