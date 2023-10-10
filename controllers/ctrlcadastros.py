from controllers.ctrlprincipal import CtrlPrincipal
from views.tela_pessoa import TelaPessoa


class CtrlCadastros:
    def __init__(self) -> None:
        pass
        
    
    def input_opcao_cadastros(self):
        opcao = CtrlPrincipal.mostra_tela_cadastros()
        
        if opcao == 2:
            opcao_pessoa = TelaPessoa.mostra_opcoes
            if opcao_pessoa == 1:
                a