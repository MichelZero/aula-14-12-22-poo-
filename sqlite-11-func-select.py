###
# autores:
# michel silva

# data: 14/12/2022
#

# importar o Sqlite3
import sqlite3 as db

def buscar(email):
 #       "SELECT * FROM pessoas"
 #        id, nome, numero, email
  sql = f"SELECT id, nome, numero, email  from pessoas WHERE email = '{email}'"
  #print(sql)
  return sql

# criar o banco ou conecta o banco
db1 = db.connect("agenda.db")


# antes devemos criar o primeiro o objeto cursor
# que vai receber o banco e assim podemos executar os comando SQL (criar tabela, inserir, excluir, etc)
cursor = db1.cursor()



#nome = input("informe um nome: ")
#numero = input("informe um número de telefone: ")
email = input("informe um email: ")

cursor.execute(buscar(email))
# no select não exite o commit
registro = cursor.fetchone()
print(registro)
print()

# para visualizar os dados da tabela
# execute um SELECT para o cursor
# print o método fetchall() (fetch -> buscar)
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall()) 
db1.close()
