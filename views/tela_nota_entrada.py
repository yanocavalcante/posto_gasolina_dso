import PySimpleGUI as sg


class TelaNotaEntrada:
    def __init__(self):
        self.__window = None
        self.input_fornecedor()

    def input_fornecedor(self):
        sg.theme('DarkAmber')
        layout = [
                  [sg.Text('Fornecedor:'), (sg.In('', key='fornecedor'))],
                  [sg.B('Confimar')]
        ]
        self.__window = sg.Window('Menu Nota de Entrada').Layout(layout)

    def open(self):
        event, values = self.__window.Read()
        return values

    def close(self):
        self.__window.Close()
