from views.tela_principal import TelaPrincipal
from controllers.ctrlcadastros import CtrlCadastros
from controllers.ctrlcaixas import CtrlCaixas
from controllers.ctrlnotas import CtrlNotas

class CtrlPrincipal:
    def __init__(self):
        pass

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
        op = TelaPrincipal.opcoes_do_sistema()
        try:
            op = int(op)

            if op not in [1, 2, 3, 4]:
                raise ValueError
        except ValueError:
            self.mostra_tela_principal()

        self.processa_input(op)

    def mostra_tela_notas(self):
        pass

    def mostra_tela_cadastros(self):
        CtrlCadastros().input_opcao_cadastros()

    def mostra_tela_financeiro(self):
        pass

    def processa_input(self, op):
        if op == 1:
            self.mostra_tela_notas()
        elif op == 2:
            self.mostra_tela_cadastros()
        elif op == 3:
            self.mostra_tela_financeiro()