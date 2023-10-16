from views.tela_principal import TelaPrincipal

class TelaCadastro(TelaPrincipal):

    def mostra_opcoes(self):
        self.limparTela()
        self.cabecalho('Cadastros')
        print('1 - Produtos        2 - Clientes        3 - Funcionários        4 - Retornar')
        op = self.le_opcoes([1,2,3,4])
        return op
