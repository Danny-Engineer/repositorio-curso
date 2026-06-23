import streamlit as st
from pathlib import Path
from config.settings import DOCS
from services.docx_service import markdown_to_simple_docx

def render_exportar():
    st.header("📄 Exportar documentos")

    md_files = sorted(DOCS.rglob("*.md"))
    if not md_files:
        st.info("Todavía no hay archivos Markdown para exportar.")
        return

    selected = st.selectbox("Selecciona un archivo Markdown", md_files, format_func=lambda p: str(p.relative_to(DOCS)))

    if st.button("Exportar a DOCX"):
        out = markdown_to_simple_docx(Path(selected))
        st.success(f"DOCX generado: {out}")
        st.code(str(out))
