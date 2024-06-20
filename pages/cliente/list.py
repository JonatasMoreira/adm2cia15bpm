import streamlit as st
import Controllers.ClienteController as ClienteController
import pages.cliente.create as pageCreateCliente

def listar():
    paramId = st.query_params.get('id')
    if paramId is None : 
        st.query_params.clear()       
        # Entre parenteses define o tamanho das colunas
        colums = st.columns((1,2,1,2,1,1))
        # list com os titulos das colunas
        campos = ['Nº', 'Nome', 'Idade', 'Profissão', 'Excluir', 'Alterar']
        # print(zip(colums,campos))
        for col, campo_nome in zip(colums,campos):
            col.write(campo_nome)
        
        for item in ClienteController.selecionarTodos():
            
            col1, col2, col3, col4, col5, col6 = st.columns((1,2,1,2,1,1))
            col1.write(item.id)
            col2.write(item.nome)
            col3.write(item.idade)
            col4.write(item.profissao)
            
            button_space_excluir = col5.empty()
            # Entre parenteses naposição 0 o texto do botao e na 1 o identificador
            on_click_excluir = button_space_excluir.button('Excluir', 'btnExcluir' + str(item.id))
            
            button_space_alterar = col6.empty()
            on_click_alterar = button_space_alterar.button('Alterar', 'btnAlterar' + str(item.id))
            
            if on_click_excluir:
                str_id=str(item.id)
                ClienteController.excluir(item.id)
                #print(str_id)
                button_space_excluir.button(
                'Excluído','btnExcluir1'+str_id)
                st.experimental_rerun() 
                # ClienteController.excluir(item.id)
                # st.experimental_rerun()
                
            if on_click_alterar:
                st.query_params = {
                    "id" : item.id
                }
                st.experimental_rerun()
                
    else:
        on_click_voltar = st.button('Voltar')
        if on_click_voltar:
            st.query_params.clear()
            st.experimental_rerun()
        pageCreateCliente.create()