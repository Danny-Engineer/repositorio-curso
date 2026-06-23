import streamlit as st
from config.settings import DOCS, ASSETS, PROMPTS, OUTPUT
from utils.helpers import count_files
from services.git_service import git_status, git_log
from services.mkdocs_service import build_site
from services.prompt_service import ensure_prompt_library

def render_dashboard():
    ensure_prompt_library()
    st.header("📊 Dashboard Ejecutivo")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Markdown", count_files(DOCS, "*.md"))
    col2.metric("Imágenes", count_files(ASSETS, "*.png") + count_files(ASSETS, "*.jpg") + count_files(ASSETS, "*.svg"))
    col3.metric("Prompts", count_files(PROMPTS, "*.md") + count_files(PROMPTS, "*.txt"))
    col4.metric("Output", count_files(OUTPUT, "*.*"))

    st.divider()
    st.subheader("Estado del entorno")
    c1, c2, c3, c4 = st.columns(4)
    c1.success("Python activo")
    c2.success("Streamlit activo")
    c3.success("Repositorio activo")
    c4.success("Prompt Library activa")

    st.divider()
    st.subheader("Acciones rápidas")
    a1, a2, a3 = st.columns(3)

    if a1.button("☁ Git status"):
        st.code(git_status())

    if a2.button("🧾 Últimos commits"):
        st.code(git_log())

    if a3.button("🌐 Construir sitio"):
        st.code(build_site())
