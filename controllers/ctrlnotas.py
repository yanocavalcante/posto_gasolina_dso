from views.tela_nota import TelaNotas
from models.notaentrada import NotaEntrada
from models.notasaida import NotaSaida


class CtrlNotas:
    def __init__(self, ctrlprincipal):
        self.__ctrlprincipal = ctrlprincipal
        self.__notas = []
        self.__telanota = TelaNotas()

    def pergunta_tipo_nota(self):
        op = self.__telanota.mostra_tipo_notas()
        self.processa_input_tipo(op)

    def cadastra_notaSaida(self):
        cliente, produtos = self.__telanota.input_notaSaida()
        num = self.calcula_num_nota()
        cliente = self.__ctrlprincipal.ctrlcadastros.verifica_lista_clientes(cliente)
        nota = NotaSaida(num, produtos, cliente)
        self.__notas.append[nota]
        nota.calcula_valor_saida
        self.__ctrlprincipal.ctrlcaixas.adiciona_movimento(nota)
        for produto in produtos:
            self.__ctrlprincipal.ctrlcadastros.diminuir_estoque(produto['qnt'], produto['nome'].nome)
        self.retornar()
        
    def cadastra_notaEntrada(self):
        fornecedor, produtos = self.__telanota.input_notaEntrada()
        num = self.calcula_num_nota()
        nota = NotaEntrada(num, produtos, fornecedor)
        self.__notas.append(nota)
        nota.calcula_valor_entrada()
        self.__ctrlprincipal.ctrlcaixas.adiciona_movimento(nota)
        for produto in produtos:
            self.__ctrlprincipal.ctrlcadastros.aumentar_estoque(produto['qnt'], produto['nome'].nome)
        self.retornar()

    def calcula_num_nota(self):
        num = len(self.__notas) + 1
        return num
        
    def retornar(self):
        self.__ctrlprincipal.mostra_tela_principal()

    def processa_input_tipo(self, op):
        if op == 1:
            self.cadastra_notaSaida()

        elif op == 2:
            self.cadastra_notaEntrada()
        
        elif op == 3:
            self.retornar()