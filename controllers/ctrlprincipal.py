from views.telaprincipal import TelaPrincipal
from controllers.ctrlcadastros import CtrlCadastros
from controllers.ctrlcaixas import CtrlCaixas
from controllers.ctrlnotas import CtrlNotas

class CtrlPrincipal:
    def __init__(self):
        self.__ctrlnotas = CtrlNotas(self)
        self.__ctrlcaixa = CtrlCaixas(self)
        self.__ctrlcadastro = CtrlCadastros(self)
        self.__telaprincipal = TelaPrincipal()

    @property
    def ctrlnotas(self):
        return self.__ctrlnotas
    
    @property
    def ctrlcaixa(self):
        return self.__ctrlcaixa
    
    @property
    def ctrlcadastro(self):
        return self.__ctrlcadastro

    def mostra_tela_principal(self):
        op = self.__telaprincipal.opcoes_do_sistema()
        self.processa_input(op)

    def processa_input(self,op):
        if op == 1:
            self.mostra_tela_notas()
        elif op == 2:
            self.mostra_tela_cadastros()
        elif op == 3:
            self.mostra_tela_financeiro()