from model_cadastrar import CadastrarSolicitanteModel

class CadastrarSolicitanteController:
    def __init__(self):
        self.model = CadastrarSolicitanteModel()

    def dadosCadastrais(self, nome, email, senha, setor):
        self.model.novoUsuario(nome, email, senha, setor)