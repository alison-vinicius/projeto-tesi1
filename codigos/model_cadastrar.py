import conexaoBD
import sqlite3

class CadastrarSolicitanteModel:
    def __init__(self):
        self.con = conexaoBD.Conexao()
        self.cursor = self.con.cursor()

    def novoUsuario(self, nome, email, senha, setor_nome):
        """
        Insere um novo usuário no banco de dados.
        Primeiro, verifica se o setor existe. Se não, o cria.
        Em seguida, insere o usuário com o ID do setor correspondente.
        """
        try:
            # 1. Obter ou criar o ID do setor
            id_setor = self._obter_ou_criar_setor(setor_nome)
            
            # 2. Inserir o novo usuário
            tipo_usuario = "solicitante"
            self.cursor.execute("""
                INSERT INTO usuario (nome, email, senha, tipoUsuario, id_setor)
                VALUES (?, ?, ?, ?, ?)
            """, (nome, email, senha, tipo_usuario, id_setor))
            self.conn.commit()
            print(f"Usuário {nome} cadastrado com sucesso!")
            return True
            
        except sqlite3.Error as e:
            print(f"Erro ao cadastrar usuário: {e}")
            self.conn.rollback() # Desfaz a transação em caso de erro
            return False
            
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
    