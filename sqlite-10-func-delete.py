###
# autores:
# michel silva

# data: 14/12/2022
#

# importar o Sqlite3
import sqlite3 as db


# a função excluir recebe 1 parâmetro email e retorna uma string com o comando SQL
def excluir(email):
#       "DELETE from pessoas WHERE idade = 9"
  sql = f"DELETE from pessoas WHERE email = '{email}'"
  #print(sql) # para testar  a string sql gerada pela função inserir
  return sql # retorna a string sql gerada pela função inserir

# criar o banco ou conecta o banco
db1 = db.connect("agenda.db")


# antes devemos criar o primeiro o objeto cursor
# que vai receber o banco e assim podemos executar os comando SQL (criar tabela, inserir, excluir, etc)
cursor = db1.cursor()



#nome = input("informe um nome: ")
#numero = input("informe um número de telefone: ")
email = input("informe um email: ")

cursor.execute(excluir(email))
db1.commit()


# para visualizar os dados da tabela
# excute um SELECT para o cursor
# print o método fetchall() (fetch -> buscar)
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall()) 
db1.close()