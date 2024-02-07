import streamlit as st
import pandas as pd

data = pd.read_csv('informacao.csv')
data

# Add a slider to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'Buscar candidato por localidade',
    (data['localidade'])
)
add_selectbox = st.sidebar.selectbox(
    'Buscar candidato por profissão',
    (data['profissao'])
)
add_selectbox = st.sidebar.selectbox(
    'Buscar candidato por cargo',
    (data['cargo_atual'])
)