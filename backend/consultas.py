import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()


cursor.execute("SELECT * FROM usuario")
resultado = cursor.fetchone()

for registro in resultado:
    print(f"Nome: {registro[0]} Telefone: {registro[1]}")


cursor.close()
conexao.close()
