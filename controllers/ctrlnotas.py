from views.tela_nota_gui import TelaNotas
from views.tela_nota_saida import TelaNotaSaida
# from views.tela_nota_entrada import TelaNotaEntrada
from models.notaentrada import NotaEntrada
from models.notasaida import NotaSaida


class CtrlNotas:
    def __init__(self, ctrlprincipal):
        self.__ctrlprincipal = ctrlprincipal
        self.__notas = []
        self.__telanota = TelaNotas()
        self.__telanota_saida = TelaNotaSaida()
        # self.__telanota_entrada = TelaNotaEntrada()

    def pergunta_tipo_nota(self):
        op = self.__telanota.open()
        self.__telanota.close()
        self.processa_input_tipo(op)

    def cadastra_notaSaida(self):
        op = True
        list_prod_nota = list()
        while op == True:
            dic_info_prod = self.__telanota.input_produtos()       #TELA_NOTA_SAIDA
            obj_prod = self.__ctrlprincipal.ctrlcadastros.verifica_lista_produtos(dic_info_prod['nome'])
            produto = {'prod': obj_prod, 'qnt': dic_info_prod['qnt']}
            list_prod_nota.append(produto)
            op = dic_info_prod['op']
        num = self.calcula_num_nota()
        cliente = self.__telanota.input_cliente()       #TELA_NOTA_SAIDA
        cliente = self.__ctrlprincipal.ctrlcadastros.verifica_lista_clientes(cliente)
        nota = NotaSaida(num, list_prod_nota, cliente)
        self.__notas.append(nota)
        nota.calcula_valor_saida
        self.__ctrlprincipal.ctrlcaixas.adiciona_movimento(nota)
        for produto in list_prod_nota:
            self.__ctrlprincipal.ctrlcadastros.diminuir_estoque(produto['qnt'], produto['prod'])
        self.retornar()
        
    def cadastra_notaEntrada(self):
        op = True
        list_prod_nota = list()
        while op == True:
            nome, qnt, op = self.__telanota.input_notaEntrada()     #TELA_NOTA_ENTRADA
            obj_prod = self.__ctrlprincipal.ctrlcadastros.verifica_lista_produtos(nome)
            produto = {'prod': obj_prod, 'qnt': qnt}
            list_prod_nota.append(produto)
        num = self.calcula_num_nota()
        fornecedor = self.__telanota.input_fornecedor()     #TELA_NOTA_ENTRADA
        nota = NotaEntrada(num, list_prod_nota, fornecedor)
        nota.calcula_valor_entrada()
        self.__notas.append(nota)
        self.__ctrlprincipal.ctrlcaixas.adiciona_movimento(nota)
        for produto in list_prod_nota:
            self.__ctrlprincipal.ctrlcadastros.aumentar_estoque(produto['qnt'], produto['prod'])
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
            self.retornar
