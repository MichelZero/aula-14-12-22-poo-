###
# autores:
# michel silva

# data: 14/12/2022
#

# importar o Sqlite3
import sqlite3 as db


# a função atualizarNome recebe 2 parâmetros nome e email e retorna uma string com o comando SQL
def atualizarNome(nome, email):
 #       "UPDATE pessoas SET idade = 20 WHERE nome = 'Dani'"
  sql = f"UPDATE pessoas SET nome = '{nome}' WHERE email = '{email}'"
 # print(sql) # para testar  a string sql gerada pela função inserir 
  return sql # retorna a string sql gerada pela função inserir

# criar o banco ou conecta o banco
db1 = db.connect("agenda.db")


# antes devemos criar o primeiro o objeto cursor
# que vai receber o banco e assim podemos executar os comando SQL (criar tabela, inserir, excluir, etc)
cursor = db1.cursor()



nome = input("informe um nome: ")
#numero = input("informe um número de telefone: ")
email = input("informe um email: ")

cursor.execute(atualizarNome(nome, email))
db1.commit()
#db1.close()  # comentei para visualizar os dados abaixo

# para visualizar os dados da tabela
# execute um SELECT para o cursor
# print o método fetchall() (fetch -> buscar)
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall()) 
db1.close()