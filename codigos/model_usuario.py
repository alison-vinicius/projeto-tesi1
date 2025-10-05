# usuario_model.py
import conexaoBD


class UsuarioModel:
    def validar_login(self, email, senha):
        """
        Valida as credenciais do usuário no banco de dados.
        Retorna os dados do usuário se for válido, senão retorna None.
        """
        banco = conexaoBD.Conexao()
        con = banco.get_conexao()
        if con is None:
            return None

        try:
            cursor = con.cursor()
            # SQL para buscar um usuário com o email e senha fornecidos
            cursor.execute("SELECT tipoUsuario FROM usuario WHERE email = ? AND senha = ?", (email, senha))
            usuario_encontrado = cursor.fetchone() # Pega o primeiro resultado
            if(usuario_encontrado):
                return usuario_encontrado[0]
            else:
                return usuario_encontrado
           
        finally:
            # Garante que a conexão seja sempre fechada
            if con:
                con.close()


   
        
        

