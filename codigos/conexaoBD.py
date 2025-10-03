import sqlite3
from sqlite3 import Error

class Conexao:
    def get_conexao(self):
        caminho = 'banco.db'
        try:
            con = sqlite3.connect(caminho)
            print(con)
            return con
        except Error as er:
            print(er)
