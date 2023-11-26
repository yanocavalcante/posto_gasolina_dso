from views.tela_caixa_gui import TelaCaixa
from models.caixa import Caixa
from models.caixa_dao import CaixaDAO


class CtrlCaixas:
    def __init__(self, ctrlprincipal):
        self.__ctrlprincipal = ctrlprincipal
        self.__telacaixa = TelaCaixa()
        self.__dao = CaixaDAO()
        self.__continua_na_tela = True

    @property
    def listacaixas(self):
        return self.__dao.get_all()
    
    def pega_caixas_nome(self):
        lista_nomes = []
        for caixa in self.listacaixas:
            lista_nomes.append(caixa.nome)
        return lista_nomes

    def pergunta_caixa(self):
        caixa = self.__telacaixa.input_caixa(self.pega_caixas_nome())
        for caixas in self.listacaixas:
            if caixa == caixas.nome:
                return caixas
        self.__telacaixa.mostra_mensagem('AVISO: Caixa Não Encontrado!')
        return

    def consulta_caixa(self):
        caixa = self.pergunta_caixa()
        dic_movimentos = {}
        for movimento in caixa.listamovimentos:
            dic_movimentos[f'{movimento.num}'] = movimento.valor
        saldo_inicial = caixa.saldo_inicial
        saldo_final = caixa.saldo
        if caixa.tipo == 'Físico':
            self.__telacaixa.imprime_historico(dic_movimentos, saldo_inicial, saldo_final)
        elif caixa.tipo == 'Bancário':
            credito = caixa.credito
            self.__telacaixa.imprime_historico(dic_movimentos, saldo_inicial, saldo_final, credito)
        self.retornar()

    def cria_caixa(self):
        tipo, nome, saldo, credito = self.__telacaixa.input_cadastro_caixa()
        caixa = Caixa(tipo, nome, saldo, credito)
        self.__dao.add(caixa)
        self.__telacaixa.mostra_mensagem('Caixa Cadastrado com Sucesso!')
        self.abre_tela()
    
    def adiciona_movimento(self, nota):
        caixa = self.pergunta_caixa()
        while caixa is None:
            caixa = self.pergunta_caixa()
        if nota.valor < 0:
            if caixa.tipo == 'Físico':
                if (caixa.saldo + nota.valor) < 0:
                    self.__telacaixa.mostra_mensagem('AVISO: Operação Cancelada!')
                    return False
            elif caixa.tipo == 'Bancário':
                if (caixa.saldo + nota.valor) < 0:
                    credito_restante = (caixa.saldo + nota.valor) + caixa.credito
                    self.__telacaixa.mostra_mensagem('AVISO: Uso de Crédito Bancário!')

                elif (caixa.saldo + caixa.credito) + (nota.valor) < 0:
                    self.__telacaixa.mostra_mensagem('AVISO: Operação Cancelada!')
                    return False
        caixa.listamovimentos.append(nota)
        caixa.calcula_novo_saldo(nota)
        self.__dao.add(caixa)
        return True

    def retornar(self):
        self.__continua_na_tela = False

    def abre_tela(self):
        self.__continua_na_tela = True
        lista_opcoes = {1: self.cria_caixa, 2: self.consulta_caixa,
                        3: self.retornar}
        
        while self.__continua_na_tela:
            lista_opcoes[self.__telacaixa.tela_acao()]()
