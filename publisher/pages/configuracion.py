import streamlit as st
from config.settings import ROOT, DOCS, ASSETS, PROMPTS, OUTPUT

def render_configuracion():
    st.header("⚙ Configuración")
    st.write(f"Ruta del proyecto: `{ROOT}`")
    st.write(f"Ruta docs: `{DOCS}`")
    st.write(f"Ruta assets: `{ASSETS}`")
    st.write(f"Ruta prompts: `{PROMPTS}`")
    st.write(f"Ruta output: `{OUTPUT}`")

    st.divider()
    st.subheader("Próximas integraciones")
    st.checkbox("OpenAI API", value=False)
    st.checkbox("Claude API", value=False)
    st.checkbox("RAG local", value=False)
    st.checkbox("n8n", value=False)
