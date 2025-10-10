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