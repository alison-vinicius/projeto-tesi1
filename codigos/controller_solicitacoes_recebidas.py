from model_solicitacao import SolicitacaoModel
class SolicitantesRecebidasController:
    def __init__(self):
        self.model = SolicitacaoModel()
    

    def obter_solicitacoes_pendentes(self):
        return self.model.buscar_solicitacoes_pendentes()