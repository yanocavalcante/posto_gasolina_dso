import os
from time import sleep


class TelaPrincipal:

    def limparTela(self):
        if os.name == 'nt': 
            os.system('cls')
        else:
            os.system('clear')
    
    def le_opcoes(self, ops):
        try:
            op = int(input())
            if op in ops:
                return op
            else:
                raise Exception
        except Exception:
            print('Valor Inválido. Redirecionando para a Tela Inicial.')
            sleep(2)
            self.opcoes_do_sistema()

    def opcoes_do_sistema(self):
        self.limparTela()
        print('-=-=-=-=-=-=-TELA INICIAL-=-=-=-=-=-=-')
        print('1 - Notas       2 - Cadastros      3 - Caixas       4 - Sair')
        op = self.le_opcoes([1,2,3,4])
        
        return op
    