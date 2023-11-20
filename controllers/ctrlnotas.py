from views.tela_nota_gui import TelaNotas
from views.tela_nota_saida import TelaNotaSaida
from views.tela_nota_entrada import TelaNotaEntrada
from models.notaentrada import NotaEntrada
from models.notasaida import NotaSaida


class CtrlNotas:
    def __init__(self, ctrlprincipal):
        self.__ctrlprincipal = ctrlprincipal
        self.__notas = []
        self.__telanota = TelaNotas()
        self.__telanota_saida = TelaNotaSaida()
        self.__telanota_entrada = TelaNotaEntrada()

    @property
    def notas(self):
        return self.__notas

    def cadastra_notaSaida(self):
        op = True
        list_prod_nota = list()
        while op == True:
            dic_info_prod = self.__telanota.input_produtos()
            obj_prod = self.__ctrlprincipal.ctrlcadastros.verifica_lista_produtos(dic_info_prod['nome'])
            produto = {'prod': obj_prod, 'qnt': int(dic_info_prod['qnt'])}
            list_prod_nota.append(produto)
            op = dic_info_prod['op']
        num = self.calcula_num_nota()
        self.__telanota_saida.input_cliente()
        values = self.__telanota_saida.open()
        cliente_string = values['cliente']
        cliente = self.__ctrlprincipal.ctrlcadastros.verifica_lista_clientes(cliente_string)
        nota = NotaSaida(num, list_prod_nota, cliente)
        self.__notas.append(nota)
        nota.calcula_valor_saida()
        self.__ctrlprincipal.ctrlcaixas.adiciona_movimento(nota)
        for produto in list_prod_nota:
            self.__ctrlprincipal.ctrlcadastros.diminuir_estoque(produto['qnt'], produto['prod'])
        self.__telanota.mostra_mensagem('Nota Cadastrada com Sucesso!')            
        self.abre_tela()

    def cadastra_notaEntrada(self):
        op = True
        list_prod_nota = list()
        while op == True:
            dic_info_prod = self.__telanota.input_produtos()
            obj_prod = self.__ctrlprincipal.ctrlcadastros.verifica_lista_produtos(dic_info_prod['nome'])
            produto = {'prod': obj_prod, 'qnt': int(dic_info_prod['qnt'])}
            list_prod_nota.append(produto)
            op = dic_info_prod['op']
        num = self.calcula_num_nota()
        self.__telanota_entrada.input_fornecedor()
        values = self.__telanota_entrada.open()
        fornecedor_string = values['fornecedor']
        nota = NotaEntrada(num, list_prod_nota, fornecedor_string)
        nota.calcula_valor_entrada()
        self.__notas.append(nota)
        self.__ctrlprincipal.ctrlcaixas.adiciona_movimento(nota)
        for produto in list_prod_nota:
            self.__ctrlprincipal.ctrlcadastros.aumentar_estoque(produto['qnt'], produto['prod'])
        self.__telanota.mostra_mensagem('Nota Cadastrada com Sucesso!')
        self.abre_tela()

    def calcula_num_nota(self):
        num = len(self.__notas) + 1
        return num

    def retornar(self):
        self.__ctrlprincipal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_notaSaida, 2: self.cadastra_notaEntrada,
                        3: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__telanota.tela_tipo_nota()]()
