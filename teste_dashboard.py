import streamlit as st
import pandas as pd
from components.kpi_media import render_kpi_media
from components.heatmap import render_heatmap

st.set_page_config(page_title="Teste Dashboard", layout="wide")

@st.cache_data
def carregar_dados(breach):
    return pd.read_csv(breach)

df = carregar_dados('data/curated/base_tratada.csv')

st.write("# Teste dos Novos Componentes (Média e Heatmap)")

st.write("---")
render_kpi_media(df)

st.write("---")
render_heatmap(df)
