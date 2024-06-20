import streamlit as st
import Controllers.ClienteController as ClienteController
import models.cliente as cliente


def create():

    idAlteracao = st.query_params
    clienteRecuperado = None
    
    if idAlteracao.get('id') != None:
        idAlteracao = idAlteracao.get('id')
        clienteRecuperado = ClienteController.selecionarById(idAlteracao)[0]
        print('id de cliente recuperado',clienteRecuperado.id, idAlteracao)
        st.query_params = {
                    "id" : clienteRecuperado.id
                }
        st.title("Alterar cliente")
    else:
        st.title("Incluir cliente")
    
        
    with st.form(key='include_cliente'):
        listOccupation = ["Dev" , "Musico", "pm", "pf", "prf"]
        
        if clienteRecuperado == None:
            input_name = st.text_input(label="Insira o seu nome")
            input_age = st.number_input(label="Insira o sua idade", format = "%d", step=1)
            input_occupation = st.selectbox("Selecione sua profissão",
                                                options= listOccupation)
        else:
            input_name = st.text_input(label="Insira o seu nome", value=clienteRecuperado.nome)
            input_age = st.number_input(label="Insira o sua idade", value=clienteRecuperado.idade, format = "%d", step=1)
            input_occupation = st.selectbox("Selecione sua profissão",
                                                options= listOccupation, index=listOccupation.index(clienteRecuperado.profissao))
            
            
        input_button_submit = st.form_submit_button("Enviar")
        
            
    if input_button_submit:
        if clienteRecuperado == None:
            ClienteController.incluir(cliente.Cliente(0, input_name, input_age, input_occupation))
            st.success("incluido com sucesso!")
        else:
            ClienteController.alterar(cliente.Cliente(clienteRecuperado.id, input_name, input_age, input_occupation))

            print(idAlteracao)
            st.success("alterado com sucesso!")
            st.query_params.clear()
            
        