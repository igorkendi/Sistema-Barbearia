import streamlit as st
import pandas as pd
import funcoes
import datetime


try:
    with open("style.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.error("Arquivo 'style.css' não encontrado. Certifique-se de que ele está na mesma pasta.")
except Exception as e:
    st.error(f"Erro ao ler o arquivo style.css: {e}")

st.set_page_config(layout="wide")

def validar_e_adcionar():
    nome = st.session_state.input_nome
    celular = st.session_state.input_celular
    horario_str = st.session_state.input_horario
    barbeiro = st.session_state.input_barbeiro

    if not nome.strip():
        st.error("Por favor, preencha o campo 'Nome'.")
        return
    
    if not celular.strip():
        st.error("Por favor, preencha o campo 'Número de contato'. ")
        return
    
    if not barbeiro.strip():
        st.error("Por favor insira o nome do 'Barbeiro'.")
    
    numero_limpo = celular.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    if not numero_limpo.isdigit():
        st.error("O número de contato deve ser apenas dígitos (e opcionalmente '()', '-', ' ').")
        return
    
    try:
        datetime.datetime.strptime(horario_str, "%H:%M")

    except ValueError:
        st.error(f"Formato de horário inválido. Use HH:MM (ex: 09:30 ou 14:45).")
        return

    try:
        
        funcoes.inserirDados(nome, celular, horario_str, barbeiro) 
        
        st.success("Horário marcado com sucesso!")
        
        
        st.session_state.input_nome = ""
        st.session_state.input_celular = ""
        st.session_state.input_horario = "" 
        st.session_state.input_barbeiro = ""

    except Exception as e:
        st.error(f"Ocorreu um erro ao salvar: {e}")

st.markdown("<h1><i class='fa-solid fa-scissors'></i> Barbearia - Insira o Nome Aqui</h1>", unsafe_allow_html=True)


st.header("Cadastro de clientes e horários")


st.subheader("Adicionar novo horário:")
st.text_input("Nome do cliente:", key ="input_nome")
st.text_input("Número do cliente:", key ="input_celular")
st.text_input("Nome do barbeiro:", key ="input_barbeiro" )
st.text_input("Horário marcado (ex: 14:30):", placeholder="HH:MM", key ="input_horario")
st.button(
        "Adicionar horário",
        on_click=validar_e_adcionar    
    )


st.divider()
with st.expander("Lista de horários marcados", expanded=True):

    try:
        dados = funcoes.listarDados()
        if dados:
            tb = pd.DataFrame(dados, columns=["ID", "Nome", "Celular", "Horario", "Barbeiro"])
            st.dataframe(tb, use_container_width=True)
        else:
            st.info("Nenhum horário cadastrado.")

    except Exception as e:
        st.error(f"Erro ao carregar a lista de horários: {e}")

    if st.button("Atualizar Lista"):
        st.rerun()

st.divider()
with st.expander("Apagar um horário", expanded=True):
    id_para_deletar = st.number_input("Digite o ID para apagar um horário", min_value=1, step=1, value=None)

    if st.button("Apagar horário"):
        if id_para_deletar:
            if funcoes.deletarHorario(id_para_deletar):
                st.success(f"Horário com ID {id_para_deletar} apagado!")
                st.rerun()
            else:
                st.error("Ocorreu um erro ao apagar o horário.")
        else:
            st.warning("Digite um ID para apagar")