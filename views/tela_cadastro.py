from views.tela_principal import TelaPrincipal, sleep
import PySimpleGUI as sg

class TelaCadastros(TelaPrincipal):
    def __init__(self):
        self.__window = None
        self.init_acao()

    def init_acao(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('---Cadastros---', font = ('Verdana', 25))],
            [sg.Text('')],
            [sg.B('Cadastrar', font = ('Verdana', 12), size=(18))],
            [sg.B('Consultar', font = ('Verdana', 12), size=(18))],
            [sg.B('Alterar', font = ('Verdana', 12), size=(18))],
            [sg.B('Excluir', font = ('Verdana', 12), size = (18))],
            [sg.T('')],
            [sg.B('Voltar', font=('Verdana', 9))]
        ]
        self.__window = sg.Window('Menu Cadastros').Layout(layout)

    def open(self):
        event, values = self.__window.Read()
        return event, values
    
    def close(self):
        self.__window.Close()

    

    #Versão Colla
    def mostra_opcoes(self,):
        self.limparTela()
        self.cabecalho('Cadastros')
        self.subcabecalho('Tipos')
        print("1 - Produtos       2 - Pessoas       3 - Voltar")
        op = self.le_opcoes([1,2,3,])
        return op
    
    def input_id_para_alterar(self):
        id_para_alterar = input("Digite o id para alterar: ")
        return id_para_alterar
    
    def opcao_alterar(self):
        nome = input("Novo nome: ")
        cpf = input("Novo cpf: ")
        telefone = input("Novo telefone: ")
        idade = input("Nova idade: ")

        return nome, idade, cpf, telefone
    
    def input_id_para_excluir(self):
        id_para_excluir = input("Digite o id da pessoa que deseja excluir: ")
        return id_para_excluir
