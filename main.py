import streamlit as st
import pages.cliente.create as PageCreateCliente
import pages.cliente.list as PageListCliente


st.sidebar.title("Menu")
page_cliente = st.sidebar.selectbox("Cliente", ["incluir", "Consultar"])

if page_cliente == "Consultar":
    PageListCliente.listar()
    
if page_cliente == "incluir":
    st.query_params.clear()
    PageCreateCliente.create()
    
