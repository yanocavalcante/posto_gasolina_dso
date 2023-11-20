import PySimpleGUI as sg


class TelaNotaSaida:
    def __init__(self):
        self.__window = None
        self.input_cliente()

    def input_cliente(self):
        sg.theme('DarkAmber')
        layout = [
                 [sg.Text('Notas', font = ('Helvica', 25))],
                 [sg.Text('Informe o Cliente da Nota:', font = ('Helvica', 15))]
                 [sg.Text('Cliente:'), (sg.In('', key='cliente'))],
                 [sg.B('Confirmar')]
        ]
        self.__window = sg.Window('Menu Nota de Saída').Layout(layout)

    def open(self):
        event, values = self.__window.Read()
        self.close()
        return values

    def close(self):
        self.__window.Close()
