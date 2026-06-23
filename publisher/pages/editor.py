import streamlit as st
from pathlib import Path
from config.settings import DOCS
from services.chapter_service import list_markdown_files, read_markdown, save_markdown

def render_editor():
    st.header("✍️ Editor Markdown")

    files = list_markdown_files()
    if not files:
        st.info("Todavía no hay archivos Markdown.")
        return

    selected = st.selectbox("Selecciona archivo", files, format_func=lambda p: str(p.relative_to(DOCS)))
    content = read_markdown(Path(selected))

    left, right = st.columns(2)

    with left:
        st.subheader("Markdown")
        edited = st.text_area("Contenido", content, height=650, label_visibility="collapsed")
        if st.button("💾 Guardar cambios"):
            save_markdown(Path(selected), edited)
            st.success("Archivo guardado correctamente.")

    with right:
        st.subheader("Vista previa")
        st.markdown(edited)
