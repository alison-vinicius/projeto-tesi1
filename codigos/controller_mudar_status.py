from model_solicitacao import SolicitacaoModel

class MudarStatusController:
    def __init__(self):
        self.model = SolicitacaoModel()
    

    def obter_todas_solicitacoes(self):
        """
        Obtém todas as solicitações e retorna a lista de dados.
        """
        return self.model.buscar_todas_solicitacoes()

    def atualizar_status(self, id_solicitacao, novo_status):
        """
        Chama a Model para atualizar o status da solicitação.
        """
        return self.model.atualizar_status_solicitacao(id_solicitacao, novo_status)