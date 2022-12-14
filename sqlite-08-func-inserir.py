###
# autores:
# michel silva

# data: 14/12/2022
#

# importar o Sqlite3
import sqlite3 as db

def inserir(nome, numero, email):
 #        INSERT INTO pessoas (nome, numero, email) 
 #        VALUES('Dani', '8395555-4444', 'dani2@gmail.com')
  sql = f"INSERT INTO pessoas (nome, numero, email) VALUES('{nome}','{numero}','{email}')"
 # print(sql)
  return sql

# criar o banco ou conecta o banco
db1 = db.connect("agenda.db")


# antes devemos criar o primeiro o objeto cursor
# que vai receber o banco e assim podemos executar os comando SQL (criar tabela, inserir, excluir, etc)
cursor = db1.cursor()



nome = input("informe um nome: ")
numero = input("informe um número de telefone: ")
email = input("informe um email: ")

cursor.execute(inserir(nome, numero, email))
db1.commit()
db1.close()