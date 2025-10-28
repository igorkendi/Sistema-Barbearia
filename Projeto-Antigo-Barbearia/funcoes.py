import sqlite3
import streamlit as st
import pandas as pd
import datetime

def conectaBD():
    conexao = sqlite3.connect("Clientes.db")
    return conexao


def inserirDados(nome, celular, horario, barbeiro):
    conexao = conectaBD()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Cliente(nome, celular, horario, barbeiro) VALUES (?, ?, ?, ?)", (nome, celular, horario, barbeiro))
    conexao.commit()
    conexao.close()


def listarDados():
    conexao = conectaBD()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Cliente ")
    dados = cursor.fetchall() #Fetchall transforma os resultados amarzenados na variavel Dados em uma lista, facilitando a manipulação.
    cursor.close()
    return dados


def deletarHorario(id_para_deletar):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        
        cursor.execute("DELETE FROM Cliente WHERE ID = ?", (id_para_deletar,))
        conexao.commit()
        conexao.close()
        return True
        
    except sqlite3.Error as e:
        print(f"Erro ao deletar: {e}")
        return False
    

       
