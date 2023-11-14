import PySimpleGUI as sg


class TelaPrincipal():
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('Postos Ypê', font = ('Helvica', 25))],
            [sg.Text('Menu Inicial:', font = ('Helvica', 15))],
            [sg.Radio('Cadastros', 'G1', key = '1')],
            [sg.Radio('Caixas', 'G1', key = '2')],
            [sg.Radio('Notas', 'G1', key = '3')],
            [sg.B('Confirmar'), sg.Exit('Sair')]
        ]
        self.__window = sg.Window('Menu Inicial').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()