import streamlit as st
import pandas as pd

data = pd.read_csv('informacao.csv')
st.dataframe(data)

# Add a slider to the sidebar:
box_local = st.sidebar.selectbox(
    'Buscar candidato por localidade',
    (data['localidade']),
    index=None,
    placeholder="Selecione a localidade",
)
box_profession = st.sidebar.selectbox(
    'Buscar candidato por profissão',
    (data['profissao']),
    index=None,
    placeholder="Selecione a profissão"
)
box_office = st.sidebar.selectbox(
    'Buscar candidato por cargo',
    (data['cargo_atual']),
    index=None,
    placeholder="Selecione o cargo"
)
#visualização-filtro
filter_local = data[data['localidade'] == box_local]
if box_local == True:
    st.write("Filtro:")
    st.write(filter_local)

# filter_profession = data[data['profissao'] == box_profession]
# if box_profession:
#     st.write("Filtro:")
#     st.write(filter_profession)

# filter_office = data[data['cargo_atual'] == box_office]
# if box_office:
#     st.write("Filtro:")
#     st.write(filter_office)