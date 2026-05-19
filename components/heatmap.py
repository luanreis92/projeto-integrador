import streamlit as st
import pandas as pd
import altair as alt

def render_heatmap(df):
    """
    Renderiza um Heatmap de Ano vs Organização.
    """
    st.write("## Concentração de Vazamentos: Ano vs Tipo de Organização")
    
    top_orgs = df['Organization type'].value_counts(normalize=True)
    df_heatmap = df.copy()
    df_heatmap['Organization type'] = df_heatmap['Organization type'].apply(
        lambda x: x if top_orgs.get(x, 0) >= 0.03 else 'Outras'
    )
    
    df_heatmap['Organization type'] = df_heatmap['Organization type'].replace({
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

    heatmap_data = df_heatmap.groupby(['Year', 'Organization type']).size().unstack(fill_value=0).stack().reset_index(name='Incidentes')
    
    base = alt.Chart(heatmap_data).encode(
        x=alt.X('Year:O', title='Ano', axis=alt.Axis(labelAngle=-45)),
        y=alt.Y('Organization type:N', title='Tipo de Organização', sort='-x'),
    )

    heatmap = base.mark_rect().encode(
        color=alt.Color('Incidentes:Q', 
                        scale=alt.Scale(scheme='blues'), 
                        legend=alt.Legend(title="Qtd Incidentes"))
    )

    text = base.mark_text(baseline='middle').encode(
        text=alt.condition(alt.datum.Incidentes > 0, 'Incidentes:Q', alt.value('')),
        color=alt.condition(
            alt.datum.Incidentes > heatmap_data['Incidentes'].max() / 2,
            alt.value('white'),
            alt.value('black')
        )
    )

    chart = (heatmap + text).properties(
        height=400
    )
    
    chart = chart.configure_scale(bandPaddingInner=0.01)
    
    st.altair_chart(chart, use_container_width=True)


