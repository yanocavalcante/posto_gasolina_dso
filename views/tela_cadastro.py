from views.tela_principal import TelaPrincipal, sleep
import PySimpleGUI as sg

class TelaCadastros(TelaPrincipal):
    def __init__(self):
        self.__window = None
        self.tela_acao()

    def mostra_mensagem(self, msg):
        sg.theme('DarkAmber')
        sg.Popup(f'{msg}', font = ('Verdana', 12))

    def input_acao(self):
        self.tela_acao()
        event, values = self.open()
        if event == 'Cadastrar':
            op = 1
        elif event == 'Alterar':
            op = 2
        elif event == 'Consultar':
            op = 3
        elif event == 'Excluir':
            op = 4
        elif event == 'Voltar':
            op = None
        self.close()
        return op

    def tela_acao(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('---Cadastros---', font = ('Verdana', 25))],
            [sg.Text('')],
            [sg.B('Cadastrar', font = ('Verdana', 12), size=(18))],
            [sg.B('Alterar', font = ('Verdana', 12), size=(18))],
            [sg.B('Consultar', font = ('Verdana', 12), size=(18))],
            [sg.B('Excluir', font = ('Verdana', 12), size = (18))],
            [sg.T('')],
            [sg.B('Voltar', font=('Verdana', 9))]
        ]
        self.__window = sg.Window('Menu Ações').Layout(layout)

    def input_categoria(self):
        self.tela_categoria()
        event, values = self.open()
        if event == 'Produtos':
            op = 1
        if event == 'Funcionários':
            op = 2
        if event == 'Clientes':
            op = 3
        self.close()
        return op

    def tela_categoria(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('---Cadastros---', font = ('Verdana', 25))],
            [sg.Text('')],
            [sg.B('Produtos', font = ('Verdana', 12), size=(18))],
            [sg.B('Funcionários', font = ('Verdana', 12), size=(18))],
            [sg.B('Clientes', font = ('Verdana', 12), size=(18))],
            [sg.T('')],
            [sg.B('Voltar', font=('Verdana', 9))]
        ]
        self.__window = sg.Window('Menu Categorias').Layout(layout)

    def open(self):
        event, values = self.__window.Read()
        return event, values
    
    def close(self):
        self.__window.Close()
