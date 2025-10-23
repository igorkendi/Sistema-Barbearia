import streamlit as st
import pandas as pd
import funcoes

st.title("Cadastro de clientes")
nome = st.text_input("Digite o nome do cliente: ")
celular = st.text_input("Digite o número de contado do cliente: ")
horario = st.text_input("Horário marcado:  ")