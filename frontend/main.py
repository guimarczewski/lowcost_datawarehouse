import streamlit as st
from datasource.csv import CSVCollector
from contract.catalogo import Catalogo

st.title("Essa é uma página de portal de dados")

catalogo_de_produto = CSVCollector(Catalogo, "C11:I211")
catalogo_de_produto.start()