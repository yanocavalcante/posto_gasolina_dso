from views.tela_nota import TelaNotas
from models.notaentrada import NotaEntrada
from models.notasaida import NotaSaida


class CtrlNotas:
    def __init__(self, ctrlprincipal):
        self.__ctrlprincipal = ctrlprincipal
        self.__notassaida = []
        self.__notasentrada = []
        self.__telanota = TelaNotas()

    def pergunta_tipo_nota(self):
        op = self.__telanota.mostra_tipo_notas()
        self.processa_input_tipo(op)

    def cadastra_notaSaida(self):
        cliente, caixa, produtos = self.__telanota.input_notaSaida()
        nota = NotaSaida(caixa, produtos, cliente)
        self.__notassaida.append(nota)
        self.retornar()
        
    def cadastra_notaEntrada(self):
        fornecedor, caixa, produtos = self.__telanota.input_notaEntrada()
        nota = NotaEntrada(caixa, produtos, fornecedor)
        self.__notasentrada.append(nota)
        self.retornar()
        
    def retornar(self):
        self.__ctrlprincipal.mostra_tela_principal()

    def processa_input_tipo(self, op):
        if op == 1:
            self.cadastra_notaSaida()

        elif op == 2:
            self.cadastra_notaEntrada()
        
        elif op == 3:
            self.retornar()