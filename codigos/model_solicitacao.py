import conexaoBD

class SolicitacaoModel:

    def vericarUsario(self, email, senha):
        banco = conexaoBD.Conexao()
        con = banco.get_conexao()

        cursor = con.cursor()

        sql = """
                SELECT usuario.id_usuario, setor.id_setor
                FROM usuario, setor
                WHERE usuario.id_setor = setor.id_setor
                AND usuario.email = ?
                AND usuario.senha = ?;
                """
        cursor.execute(sql, (email, senha))
        ids = cursor.fetchall()
        con.close()
        return ids
    
    def inserir_solicitacao(self,id_usuario, id_setor, quantidade,observacao):
        banco = conexaoBD.Conexao()
        con = banco.get_conexao()

        cursor = con.cursor()

        sql = """
                INSERT INTO solicitacao (id_usuario, id_setor, quantidade, observacao)
                VALUES (?, ?, ?, ?)
            """
        
        cursor.execute(sql, (id_usuario, id_setor, quantidade, observacao))
        con.commit()
        con.close()
        return True
    
    def buscar_solicitacoes_usuario(self, email, senha):
        banco = conexaoBD.Conexao()
        con = banco.get_conexao()

        cursor = con.cursor()

        # 1. Encontrar o id_usuario com base no email e senha
        sql_id_usuario = "SELECT id_usuario FROM usuario WHERE email = ? AND senha = ?"
        cursor.execute(sql_id_usuario, (email, senha))
        resultado_id = cursor.fetchone()

        if not resultado_id:
            return None  
            
        id_usuario = resultado_id[0]
            
        # 2. Selecionar as solicitações para este id_usuario
        sql_solicitacoes = """
            SELECT quantidade, dataSolicitacao, status
            FROM solicitacao
            WHERE id_usuario = ?
            ORDER BY dataSolicitacao DESC
            """
        cursor.execute(sql_solicitacoes, (id_usuario,))
            
        solicitacoes = cursor.fetchall()
        return solicitacoes