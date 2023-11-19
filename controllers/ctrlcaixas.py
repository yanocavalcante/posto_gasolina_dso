# from views.tela_caixa import TelaCaixa
from views.tela_caixa_gui import TelaCaixa
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
        self.__telacaixa.input_caixa()
        event, values = self.__telacaixa.open()
        for caixas in self.listacaixas:
            if values['nome'] == caixas.nome:
                return caixas
        self.__telacaixa.mostra_mensagem('AVISO: Caixa Não Encontrado!')
        self.pergunta_caixa()

    def consulta_caixa(self):
        caixa = self.pergunta_caixa()
        self.__telacaixa.imprime_historico(caixa.listamovimentos, caixa)
        self.retornar()

    def cria_caixa(self):
        event, values = self.__telacaixa.input_cadastro_caixa()
        if values['fisico']:
            tipo = 'Físico'
        elif values['bancario']:
            tipo = 'Bancário'
        nome = values['nome']
        saldo = values['saldo']
        credito = values['credito']
        caixa = Caixa(tipo, nome, saldo, credito)
        self.__listacaixas.append(caixa)
        self.retornar()
    
    def adiciona_movimento(self, nota):
        caixa = self.pergunta_caixa()
        if nota.valor < 0:
            if caixa.tipo == 'Físico':
                if (caixa.saldo + nota.valor) < 0:
                    self.__telacaixa.mostra_mensagem('AVISO: Operação Cancelada!')
                    return
            elif caixa.tipo == 'Bancário':
                if (caixa.saldo + nota.valor) < 0:
                    credito_restante = (caixa.saldo + nota.valor) + caixa.credito
                    self.__telacaixa.mostra_mensagem('AVISO: Uso de Crédito Bancário!')

                elif (caixa.saldo + caixa.credito) + (nota.valor) < 0:
                    self.__telacaixa.mostra_mensagem('AVISO: Operação Cancelada!')
                    return
        caixa.listamovimentos.append(nota)
        caixa.calcula_novo_saldo(nota)

    def retornar(self):
        self.__ctrlprincipal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cria_caixa, 2: self.consulta_caixa,
                        3: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__telacaixa.tela_acao()]()