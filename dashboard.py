import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("# Segurança Cibernética - Dashboard")

@st.cache_data
def carregar_dados(breach):
    dados_breach = pd.read_csv(breach)
    return dados_breach

df = carregar_dados('data/curated/base_tratada.csv')

st.write("## Visão Geral dos Dados")
st.dataframe(df)

st.write("## Vazamentos por Ano")
vazamentos_por_ano = df.groupby('Year').size().reset_index(name='Total de Vazamentos')
st.bar_chart(vazamentos_por_ano.set_index('Year'))

st.write("## Tipos de Organização")
org_counts = df.groupby('Organization type').size().reset_index(name='Total')
org_counts['pct'] = org_counts['Total'] / org_counts['Total'].sum()
org_counts['Organization type'] = org_counts.apply(
    lambda r: r['Organization type'] if r['pct'] >= 0.03 else 'Outras', axis=1
) # Junta todas as organizações com menos de 3% em uma categoria "Outras"

org_counts['Organization type'] = org_counts['Organization type'].replace({
    'technology': 'Tecnologia', 
    'healthcare': 'Saúde', 
    'social media': 'M. Sociais', 
    'financial': 'Finanças', 
    'academic': 'Acadêmico', 
    'government': 'Governo', 
    'retail': 'Varejo', 
    'gaming' : 'Jogos', 
    'telecoms': 'Telecomunicações'
    })
org_counts = org_counts.groupby('Organization type', as_index=False)['Total'].sum()
fig, ax = plt.subplots()
ax.pie(org_counts['Total'], labels=org_counts['Organization type'], autopct='%1.1f%%')
st.pyplot(fig)


st.write("## Métodos que geraram maior volume de vazamento")
metodos_counts = df.groupby('Method')['Records'].sum().nlargest(5).reset_index(name='Total de Registros')
metodos_counts['Method'] = metodos_counts['Method'].replace({
    'accidentally published': 'Publicação Acidental',
    'cyber attack': 'Ataque Cibernético',
    'poor security / hacked' : 'Hackeado',
    'security failure': 'Falha de Segurança',
    'unknown': 'Desconhecido'
})

st.bar_chart(metodos_counts.set_index('Method'))