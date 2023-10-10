from views.telacaixa import TelaCaixa
from models.caixa import Caixa


class CtrlCaixas:
    def __init__(self, ctrlprincipal):
        self.__ctrlprincipal = ctrlprincipal
        self.__telacaixa = TelaCaixa()
        self.__listacaixas = []
        
    def pergunta_caixa(self):
        caixa = self.__telacaixa.seleciona_caixa
        for caixas in self.__listacaixas:
            if caixa == caixas.nome:
                pass

    def pergunta_acao(self):
        op = self.__telacaixa.seleciona_acao
        if op == 1:
            self.cria_caixa
        
        elif op == 2:
            self.pergunta_caixa