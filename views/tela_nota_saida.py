import PySimpleGUI as sg


class TelaNotaSaida:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('DarkAmber')
        layout = [
                  [sg.Text('NOTA DE SAÍDA')],
                  [sg.Text('Vai romar no cu iago')]
        ]
    
    def open(self):
        event, values = self.__window.Read()
        if event == sg.WINDOW_CLOSED or event == 'Voltar':
            return event
        else:
            return values
