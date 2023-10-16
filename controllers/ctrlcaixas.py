from views.tela_caixa import TelaCaixa
from models.caixa import Caixa


class CtrlCaixas:
    def __init__(self, ctrlprincipal):
        self.__ctrlprincipal = ctrlprincipal
        self.__telacaixa = TelaCaixa()
        self.__listacaixas = []

    @property
    def listacaixas(self):
        return self.__listacaixas
        
    def pergunta_caixa(self):
        caixa = self.__telacaixa.seleciona_caixa()
        for caixas in self.listacaixas:
            print('Entrou no For')
            if caixa == caixas.nome:
                return caixas
        print('Não Funcionou')

    def consulta_caixa(self):
        caixa = self.pergunta_caixa()
        self.__telacaixa.imprime_historico(caixa.listamovimentos, caixa)
        self.retornar()

    def cria_caixa(self):
        tipo, nome, saldo, credito = self.__telacaixa.input_info_caixa()
        caixa = Caixa(tipo, nome, saldo, credito)
        self.__listacaixas.append(caixa)
        self.retornar()
    
    def retornar(self):
        self.__ctrlprincipal.mostra_tela_principal()
    
    def adiciona_movimento(self, nota):
        caixa = self.pergunta_caixa()
        caixa.listamovimentos.append(nota)
        caixa.calcula_novo_saldo(nota)

    def pergunta_acao(self):
        op = self.__telacaixa.seleciona_acao()
        if op == 1:
            self.cria_caixa()
        
        elif op == 2:
            self.consulta_caixa()
        
        elif op == 3:
            self.retornar()