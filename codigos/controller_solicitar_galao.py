from model_solicitacao import SolicitacaoModel
class SolicitarGalaoController:
    def __init__(self,email, senha):
        self.email = email
        self.senha = senha
        self.solicitacao_model = SolicitacaoModel()

    def id_setor_e_usuario(self, email, senha):
        ids = self.solicitacao_model.vericarUsario(email, senha)
        return ids




    def solicitar(self, quantidade, observacao):
        setor_usuario = self.id_setor_e_usuario(self.email, self.senha)
        tupla = setor_usuario[0]
        id_usuario = tupla[0]
        id_setor = tupla[1]

        estado = self.solicitacao_model.inserir_solicitacao(id_usuario, id_setor, quantidade,observacao)
        return estado




        # quantidade = int(quantidade)
        # print(id_usuario,id_setor)
        # print(quantidade, observacao)
        # print(type(quantidade))
    
