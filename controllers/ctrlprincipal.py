# from views.tela_principal import TelaPrincipal
from views.tela_principal_gui import TelaPrincipal
from controllers.ctrlcadastros import CtrlCadastros
from controllers.ctrlcaixas import CtrlCaixas
from controllers.ctrlnotas import CtrlNotas

class CtrlPrincipal:
    def __init__(self):
        self.__ctrlcadastros = CtrlCadastros(self)
        self.__ctrlcaixas = CtrlCaixas(self)
        self.__ctrlnotas = CtrlNotas(self)
        self.__telaprincipal = TelaPrincipal()

    @property
    def ctrlnotas(self):
        return self.__ctrlnotas
    
    @property
    def ctrlcaixas(self):
        return self.__ctrlcaixas
    
    @property
    def ctrlcadastros(self):
        return self.__ctrlcadastros

    def mostra_tela_principal(self):
        button, values = self.__telaprincipal.open()
        self.__telaprincipal.close()
        self.processa_input(values)

    def mostra_tela_notas(self):
        self.ctrlnotas.pergunta_tipo_nota()

    def mostra_tela_cadastros(self):
        self.ctrlcadastros.input_opcao_cadastros()

    def mostra_tela_caixas(self):
        self.ctrlcaixas.pergunta_acao()

    def encerra_sistema(self):
        exit(1)

    def processa_input(self, values):
        if values['3']:
            self.mostra_tela_notas()
        elif values['1']:
            self.mostra_tela_cadastros()
        elif values['2']:
            self.mostra_tela_caixas()
