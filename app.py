import streamlit as st
import datetime
from validation_utils import cpf_validator, email_validator, phone_validator
from controler import insert_student

st.title('Gerenciamento de estudantes')
st.header('Escolha uma das opções:')

# Inicializa estado, se necessário
if "first_option" not in st.session_state:
    st.session_state.first_option = None


if st.button('Inserir aluno'):
    st.session_state.first_option = "inserir"
if st.button('Editar aluno'):
    st.session_state.first_option = "editar"
if st.button('Listar alunos'):
    st.session_state.first_option = "listar"


if st.session_state.first_option == "inserir":
    full_name = st.text_input("Digite o nome completo do aluno")
    gender = st.selectbox(label="Gênero", options=["Masculino", "Feminino"])
    cpf = st.text_input(label="CPF do aluno")
    status = st.selectbox(label="Status do aluno", options=["Ativo", "Inativo"])
    telefone = st.text_input("Digite o telefone")
    email = st.text_input("Digite o e-mail do aluno ou dos responsáveis")

    if st.button("Enviar"):
        erros = []
        if not cpf_validator(cpf):
            erros.append("CPF inválido")
        if not email_validator(email):
            erros.append("E-mail inválido")
        if not phone_validator(telefone):
            erros.append("Telefone inválido")

        if erros:
            for erro in erros:
                st.error(erro)
        else:
            success, message = insert_student(name=full_name, gender=gender, cpf=cpf,
                                            status=status, phone=telefone, email=email)
            if success:
                st.success(message)
            else:
                st.error(message)
        

elif st.session_state.first_option == "editar":
    st.info("Função de edição ainda não implementada.")

elif st.session_state.first_option == "listar":
    st.info("Função de listagem ainda não implementada.")
    print("Inicando listagem")

#streamlit run app.py