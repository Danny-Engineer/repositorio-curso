import streamlit as st
from services.mkdocs_service import build_site, serve_command

def render_mkdocs():
    st.header("🌐 MkDocs")

    if st.button("Construir sitio"):
        st.code(build_site())

    st.write("Para ver el sitio local ejecuta en terminal:")
    st.code(serve_command())
