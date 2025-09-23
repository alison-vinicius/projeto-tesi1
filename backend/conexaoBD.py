import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE usuario(nome text, telefone text)
''')

cursor.execute('''
    INSERT INTO usuario(nome, telefone) values("Alison", 984182385)
    
''')

cursor.execute('''
    INSERT INTO usuario(nome, telefone) values("chaves", 123456789)
''')

cursor.execute('''
    INSERT INTO usuario(nome, telefone) values("leo", 123456782)
''')



conexao.commit()
cursor.close()
conexao.close()