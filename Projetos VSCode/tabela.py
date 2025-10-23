import sqlite3

conexao = sqlite3.connect("Clientes.db")

cursor = conexao.cursor() #Cursor é um mensageiro que envia comandos SQL ao nosso comando de dados, ele também recebe.

cursor.execute(
    """
        CREATE TABLE Cliente(
            ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL,
            Celular TEXT NOT NULL,
            Horario TEXT NOT NULL
        );
    """
)


cursor.close()
print("Tabela criada com sucesso!")


cursor.execute(
    """
        ALTER TABLE Cliente RENAME TO horario




    """
)