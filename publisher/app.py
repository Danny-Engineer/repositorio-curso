import streamlit as st
from pages.dashboard import render_dashboard
from pages.capitulos import render_capitulos
from pages.editor import render_editor
from pages.ia_assistant import render_ia_assistant
from pages.prompts import render_prompts
from pages.roadmap import render_roadmap
from pages.exportar import render_exportar
from pages.github import render_github
from pages.mkdocs_page import render_mkdocs
from pages.configuracion import render_configuracion

st.set_page_config(
    page_title="Logística IA Lab Publisher",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("📚 Logística IA Lab")
option = st.sidebar.radio(
    "Módulos",
    [
        "Dashboard",
        "Capítulos",
        "Editor Markdown",
        "IA Assistant",
        "Prompts",
        "Roadmap",
        "Exportar",
        "GitHub",
        "MkDocs",
        "Configuración",
    ],
)

st.title("📚 Logística IA Lab Publisher")
st.caption("Suite editorial para cursos, manuales, documentación técnica, RAG e IA empresarial")

if option == "Dashboard":
    render_dashboard()
elif option == "Capítulos":
    render_capitulos()
elif option == "Editor Markdown":
    render_editor()
elif option == "IA Assistant":
    render_ia_assistant()
elif option == "Prompts":
    render_prompts()
elif option == "Roadmap":
    render_roadmap()
elif option == "Exportar":
    render_exportar()
elif option == "GitHub":
    render_github()
elif option == "MkDocs":
    render_mkdocs()
elif option == "Configuración":
    render_configuracion()
