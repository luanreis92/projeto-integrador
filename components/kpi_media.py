import streamlit as st

def render_kpi_media(df):
    """
    Renderiza os KPIs de Média e Total de Registros Vazados.
    """
    media_vazamentos = df['Records'].mean()
    total_vazamentos = df['Records'].sum()
    
    def format_number(num):
        if num >= 1e9:
            return f"{num/1e9:.2f} Bilhões"
        elif num >= 1e6:
            return f"{num/1e6:.2f} Milhões"
        elif num >= 1e3:
            return f"{num/1e3:.2f} Mil"
        else:
            return f"{num:.0f}"

    st.markdown("### 📊 Indicadores Principais")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"**Média de Registros Vazados (por incidente)**\n\n# {format_number(media_vazamentos)}")
    with col2:
        st.success(f"**Total Absoluto de Registros Vazados**\n\n# {format_number(total_vazamentos)}")

