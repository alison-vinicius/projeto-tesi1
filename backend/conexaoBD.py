import sqlite3
from sqlite3 import Error


# class Conexao:
#     def get_conexao(self):
#         caminho = 'banco.db'
#         try:
#             con = sqlite3.connect(caminho)
#             return con
#         except Error as er:
#             print(er)
        
caminho = 'banco.db'
con = sqlite3.connect(caminho)

cursor = con.cursor()

