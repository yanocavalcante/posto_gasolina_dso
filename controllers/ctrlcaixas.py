from views.tela_caixa import TelaCaixa
from models.caixa import Caixa


class CtrlCaixas:
    def __init__(self, ctrlprincipal):
        self.__ctrlprincipal = ctrlprincipal
        self.__telacaixa = TelaCaixa()
        self.__listacaixas = []

        #delete-me
        self.instancia_teste()
    
    def instancia_teste(self):
        posto = Caixa('Físico', 'Posto', 2000)
        self.__listacaixas.append(posto)

    @property
    def listacaixas(self):
        return self.__listacaixas
        
    def pergunta_caixa(self):
        caixa = self.__telacaixa.seleciona_caixa()
        for caixas in self.listacaixas:
            if caixa == caixas.nome:
                return caixas
        self.__telacaixa.caixa_n_encontrado()
        self.pergunta_caixa()

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
        if nota.valor < 0:
            if caixa.tipo == 'Físico':
                if (caixa.saldo + nota.valor) < 0:
                    self.__telacaixa.cancela_operacao()
                    return
            elif caixa.tipo == 'Bancário':
                if (caixa.saldo + nota.valor) < 0:
                    saldo_negativo = (caixa.saldo + nota.valor) + caixa.credito
                    self.__telacaixa.uso_saldo(saldo_negativo)

                elif (caixa.saldo + caixa.credito) + (nota.valor) < 0:
                    self.__telacaixa.cancela_operacao()
                    return
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