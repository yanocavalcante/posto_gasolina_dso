from views.tela_cadastro import TelaCadastros
from views.tela_pessoa import TelaPessoa


class CtrlCadastros:
    def __init__(self) -> None:
        pass
        
    
    def input_opcao_cadastros(self):
        opcao = TelaCadastros().mostra_opcoes()
        
        if opcao == 2:
            opcao_pessoa = TelaPessoa().mostra_opcoes_pessoa()
            if opcao_pessoa == 1:
                info_pessoa = TelaPessoa().input_cadastro_pessoa()
                breakpoint()