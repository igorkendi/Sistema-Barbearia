import sqlite3

def conectaBD():
    conexao = sqlite3.connect("Clientes.db")
    return conexao


def inserirDados(nome, celular, horario):
    conexao = conectaBD()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO TABLE Cliente(nome, celular, endereco) VALUES (?, ?, ?)", (nome, celular, horario))
    conexao.commit()
    conexao.close()


def listarDados(): #Retorna todos os registros da tabela Cliente
    conexao = conectaBD
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Cliente ")
    dados = cursor.fetchall() #Fetchall transforma os resultados amarzenados na variavel Dados em uma lista, facilitando a manipulação.
    return dados