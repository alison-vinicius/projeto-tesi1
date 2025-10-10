# usuario_model.py
import conexaoBD
import sqlite3

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

    
    def novoUsuario(self, nome, email, senha, setor_nome):
        banco = conexaoBD.Conexao()
        con = banco.get_conexao()
        if con is None:
            return None
        try:
            id_setor = self._obter_ou_criar_setor(setor_nome)
            tipo_usuario = "solicitante"
            self.cursor.execute("""
                INSERT INTO usuario (nome, email, senha, tipoUsuario, id_setor)
                VALUES (?, ?, ?, ?, ?)
            """, (nome, email, senha, tipo_usuario, id_setor))
            self.conn.commit()
            print(f"Usuário {nome} cadastrado com sucesso!")
            return True
        finally:
            if con:
                con.close()
        
    

    def _obter_ou_criar_setor(self, setor_nome):
        """
        Verifica se um setor existe. Se existir, retorna o ID. 
        Se não, cria o setor e retorna o novo ID.
        """
        self.cursor.execute("SELECT id_setor FROM setor WHERE nome = ?", (setor_nome,))
        result = self.cursor.fetchone()
        
        if result:
            # O setor já existe
            return result[0]
        else:
            # O setor não existe, então o criamos
            self.cursor.execute("INSERT INTO setor (nome) VALUES (?)", (setor_nome,))
            self.conn.commit()
            print(f"Setor '{setor_nome}' criado.")
            return self.cursor.lastrowid # Retorna o ID do último item inserido
        

    def buscar_todos_funcionarios(self):
        banco = conexaoBD.Conexao()
        con = banco.get_conexao()
        
        try:
            cursor = con.cursor()
            sql = """
            SELECT u.id_usuario, u.nome, u.email, u.senha, u.tipoUsuario, s.nome
            FROM usuario AS u
            INNER JOIN setor AS s ON u.id_setor = s.id_setor
            WHERE u.tipoUsuario = 'funcionario'
            ORDER BY u.nome ASC
            """
            cursor.execute(sql)
            funcionarios = cursor.fetchall()
            return funcionarios
        
        except sqlite3.Error as e:
            print(f"Erro ao buscar funcionários: {e}")
            return []
        finally:
            if con:
                con.close()

    def adicionar_funcionario(self, nome, email, senha, id_setor):
        banco = conexaoBD.Conexao()
        con = banco.get_conexao()
        
        try:
            cursor = con.cursor()
            sql = "INSERT INTO usuario (nome, email, senha, tipoUsuario, id_setor) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(sql, (nome, email, senha, "funcionario", id_setor))
            con.commit()
            return True
        
        except sqlite3.Error as e:
            print(f"Erro ao adicionar funcionário: {e}")
            # Se a inserção falhar, você deve fazer um rollback para evitar estados inconsistentes
            con.rollback()
            return False
        finally:
            if con:
                con.close()
    
    def remover_funcionario(self, id_usuario):
        banco = conexaoBD.Conexao()
        con = banco.get_conexao()

        try:
            cursor = con.cursor()
            sql = "DELETE FROM usuario WHERE id_usuario = ?"
            cursor.execute(sql, (id_usuario,))
            con.commit()
            return True
        
        except sqlite3.Error as e:
            print(f"Erro ao remover funcionário: {e}")
            con.rollback()
            return False
        finally:
            if con:
                con.close()

    
    
    


    




   
        
        

