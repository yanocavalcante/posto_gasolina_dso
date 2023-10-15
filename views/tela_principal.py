import os

class TelaPrincipal:

    def limparTela(self):
        if os.name == 'nt': 
            os.system('cls')
        else:
            os.system('clear')

    def opcoes_do_sistema(self):
        self.limparTela()
        print('-=-=-=-=-=-=-TELA INICIAL-=-=-=-=-=-=-')
        print('1 - Notas       2 - Cadastros      3 - Caixas       4 - Sair')
        op = int(input())
        
        return op
    