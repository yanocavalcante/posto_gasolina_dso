import PySimpleGUI as sg


class TelaNotas():
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
                  [sg.Text('Notas', font = ('Helvica', 25))],
                  [sg.Text('Opções:', font = ('Helvica', 15))],
                  [sg.Radio('Saída', 'G1', key = '1')],
                  [sg.Radio('Entrada', 'G1', key = '2')],
                  [sg.B('Confirmar'), sg.B('Voltar')]
        ]
        self.__window = sg.Window('Menu - Notas').Layout(layout)

    def open(self):
        event, values = self.__window.Read()
        if event == sg.WINDOW_CLOSED or event == 'Voltar':
            return event
        else:
            return values

    def close(self):
        pass
