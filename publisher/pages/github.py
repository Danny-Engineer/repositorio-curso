import streamlit as st
from services.git_service import git_status, git_push, git_log, git_pull

def render_github():
    st.header("☁ GitHub")

    col1, col2, col3 = st.columns(3)

    if col1.button("Ver estado"):
        st.code(git_status())

    if col2.button("Ver historial"):
        st.code(git_log())

    if col3.button("Pull"):
        st.code(git_pull())

    st.divider()
    message = st.text_input("Mensaje de commit", "Actualización desde Publisher")
    if st.button("Commit y Push"):
        st.code(git_push(message))
