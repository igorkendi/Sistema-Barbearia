import sqlite3

conexao = sqlite3.connect("Clientes.db")
cursor = conexao.cursor()


cursor.execute("ALTER TABLE Cliente ADD COLUMN Barbeiro TEXT NOT NULL;")

conexao.commit()

conexao.close()