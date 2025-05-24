import streamlit as st
import datetime
from validation_utils import cpf_validator, email_validator, phone_validator
from controler import insert_student, delete_student_by_cpf, update_student_by_cpf

st.title('Gerenciamento de estudantes')
st.header('Escolha uma das opções:')

# Inicializa estado, se necessário
if "first_option" not in st.session_state:
    st.session_state.first_option = None


if st.button('Inserir aluno'):
    st.session_state.first_option = "inserir"
if st.button('Remover aluno'):
    st.session_state.first_option = "remover"
if st.button('Editar aluno'):
    st.session_state.first_option = "editar"    


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
        
elif st.session_state.first_option == "remover":
    cpf = st.text_input("Digite o CPF do aluno a ser excluído")
    password_del = st.text_input("Digite a senha para excluir")
    if st.button("Deletar"):
        if password_del == "AbC52@":
            success, message = delete_student_by_cpf(cpf)
            if success:
                st.success(message)
            else:
                st.error(message)
        else:
            st.error("Senha incorreta")

elif st.session_state.first_option == "editar":
    cpf = st.text_input("Digite o CPF do aluno")
    password_edit = st.text_input("Digite a senha para editar")

    st.text("Digite as novas informações do aluno")
    new_full_name = st.text_input("Digite o nome completo do aluno")
    new_gender = st.selectbox(label="Gênero", options=["Masculino", "Feminino"])
    new_status = st.selectbox(label="Status do aluno", options=["Ativo", "Inativo"])
    new_telefone = st.text_input("Digite o telefone")
    new_email = st.text_input("Digite o e-mail do aluno ou dos responsáveis")
    if st.button("Editar"):
        if password_edit == "AbC52@":
            errors = []
            if not email_validator(new_email):
                errors.append("E-mail inválido")
            if not phone_validator(new_telefone):
                errors.append("Telefone inválido")  
            if errors:
                for error in errors:
                    st.error(error)
            
            success, message = update_student_by_cpf(cpf=cpf, name=new_full_name, gender=new_gender,
                                                     status=new_status, phone=new_telefone, email=new_email)
            if success:
                st.success(message)
            else:
                st.error(message)

#streamlit run app.py