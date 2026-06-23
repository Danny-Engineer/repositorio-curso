import streamlit as st
from services.prompt_service import ensure_prompt_library, list_prompts, read_prompt

def render_prompts():
    st.header("🧠 Biblioteca de Prompts")
    ensure_prompt_library()

    prompts = list_prompts()
    selected = st.selectbox("Selecciona prompt", prompts, format_func=lambda p: p.name)

    content = read_prompt(selected)
    st.text_area("Prompt", content, height=300)
