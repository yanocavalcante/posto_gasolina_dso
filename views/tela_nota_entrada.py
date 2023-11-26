import PySimpleGUI as sg


class TelaNotaEntrada:
    def __init__(self):
        self.__window = None
        self.input_fornecedor()

    def input_fornecedor(self):
        sg.theme('DarkAmber')
        layout = [
                  [sg.Text('Notas - Entrada', font = ('Verdana', 25))],
                  [sg.Text('Informe o Fornecedor:', font = ('Verdana', 15))],
                  [sg.Text('Fornecedor:', font=('Verdana')), (sg.In('', key='fornecedor'))],
                  [sg.B('Confirmar', font=('Verdana'))]
        ]
        self.__window = sg.Window('Menu Nota de Entrada').Layout(layout)

    def open(self):
        event, values = self.__window.Read()
        self.close()
        return values

    def close(self):
        self.__window.Close()
