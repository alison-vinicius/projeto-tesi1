import conexaoBD 

banco = conexaoBD.Conexao()
con = banco.get_conexao()
cursor = con.cursor()
email = "fred@gmail.com"
senha = "123"
cursor.execute("SELECT tipoUsuario FROM usuario WHERE email == ? AND senha == ?", (email, senha))
result = cursor.fetchone()
print(result[0])


