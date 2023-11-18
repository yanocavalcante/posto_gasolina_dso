import PySimpleGUI as sg


class TelaNotaSaida:
    def __init__(self):
        self.__window = None
        self.input_cliente()

    def input_cliente(self):
        sg.theme('DarkAmber')
        layout= [
                 [sg.Text('Cliente:'), (sg.In('', key='cliente'))],
                 [sg.B('Confirmar')]
        ]
        self.__window = sg.Window('Sistema').Layout(layout)

    def open(self):
        event, values = self.__window.Read()
        return values

    def close(self):
        self.__window.Close()
