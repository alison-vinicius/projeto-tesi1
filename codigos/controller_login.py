from model_usuario import UsuarioModel
class LoginController:
    def __init__(self):
        self.usuario_model = UsuarioModel()

    def fazer_login(self, email, senha):

        tipo_usuario = self.usuario_model.validar_login(email, senha)
        
        if tipo_usuario:
            return (True, "Login bem-sucedido!", tipo_usuario)
        else:
            return (False, "Email ou senha inválidos.", None)
    