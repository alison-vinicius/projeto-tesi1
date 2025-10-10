from model_solicitacao import SolicitacaoModel

class AcompanharEntregaController:
    def __init__(self):
        self.model = SolicitacaoModel()
        
    def obter_solicitacoes(self, email, senha):
        """
        Obtém as solicitações do usuário e retorna a lista de dados.
        """
        return self.model.buscar_solicitacoes_usuario(email, senha)