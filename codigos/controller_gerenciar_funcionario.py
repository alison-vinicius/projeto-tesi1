# AdminController.py

from model_usuario import UsuarioModel

class GerenciarFuncionariosController:
    def __init__(self):
        self.model = UsuarioModel()

    def obter_todos_funcionarios(self):
        """Retorna a lista de todos os funcionários."""
        return self.model.buscar_todos_funcionarios()
        
    def adicionar_novo_funcionario(self, nome, email, senha):
        """Chama a model para adicionar um novo funcionário. O id_setor 'SGG' será tratado aqui."""
        # Primeiro, obtenha o id_setor de "SGG" (Setor de Gerenciamento de Galões)
        # Você precisará de um método na sua Model para buscar o ID do setor pelo nome.
        # Por simplicidade, vamos supor que o ID do setor 'SGG' é 1.
        id_setor_sgg = 1
        return self.model.adicionar_funcionario(nome, email, senha, id_setor_sgg)

    def remover_funcionario_existente(self, id_usuario):
        """Chama a model para remover um funcionário."""
        return self.model.remover_funcionario(id_usuario)
    