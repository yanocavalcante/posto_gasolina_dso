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
    
    def inicializa_sistema(self):
        self.abre_tela()

    def mostra_tela_notas(self):
        self.ctrlnotas.abre_tela()

    def mostra_tela_cadastros(self):
        self.ctrlcadastros.abre_tela()

    def mostra_tela_caixas(self):
        self.ctrlcaixas.abre_tela()

    def encerra_sistema(self):
        exit(1)

    def abre_tela(self):
        lista_opcoes = {1: self.mostra_tela_cadastros, 2: self.mostra_tela_caixas,
                        3: self.mostra_tela_notas, 4: self.encerra_sistema}
        while True:
            op = self.__telaprincipal.open()
            op_escolhida = lista_opcoes[op]
            self.__telaprincipal.close()
            op_escolhida()
