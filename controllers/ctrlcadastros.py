from views.tela_cadastro import TelaCadastro
from views.tela_pessoa import TelaPessoa


class CtrlCadastros:
    def __init__(self, ctrlprincipal) -> None:
        self.__ctrlprincipal = ctrlprincipal
        self.__tela_cadastro = TelaCadastro()
        

    def pergunta_categoria(self):
        op = self.__tela_cadastro.mostra_opcoes()
        if op == 1:
            self.cadastra_produto()
        elif op == 2:
            self.cadastra_cliente()
        elif op == 3:
            self.cadastra_funcionario()
        