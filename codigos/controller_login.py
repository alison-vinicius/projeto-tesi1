from model_usuario import UsuarioModel
class LoginController:
    def __init__(self):
        self.usuario_model = UsuarioModel
    def fazer_login(self, email, senha):

        usuario_encontrado = self.usuario_model.validar_login(self, email, senha)
        
        if usuario_encontrado:
            return True, "Login bem-sucedido!"
        else:
            return False, "Email ou senha inválidos."