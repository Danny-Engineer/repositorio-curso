import streamlit as st
from services.chapter_service import MODULES, create_chapter

def render_capitulos():
    st.header("📖 Generador Inteligente de Capítulos")

    module = st.selectbox("Selecciona el módulo", MODULES)
    number = st.text_input("Número del capítulo", "02")
    title = st.text_input("Título del capítulo")
    author = st.text_input("Autor", "Daniel Melchor Pérez")
    duration = st.text_input("Duración estimada", "60 minutos")
    level = st.selectbox("Nivel", ["Básico", "Intermedio", "Avanzado", "Ejecutivo"])

    objectives = st.text_area("Objetivos de aprendizaje", "Comprender...\nAplicar...\nDiseñar...")
    competencies = st.text_area("Competencias", "Pensamiento crítico\nUso de IA\nAutomatización")
    summary = st.text_area("Resumen ejecutivo", "Este capítulo introduce...")

    if st.button("🚀 Generar capítulo"):
        if not title.strip():
            st.error("Debes escribir el título del capítulo.")
        else:
            path = create_chapter(module, number, title, author, duration, level, objectives, competencies, summary)
            st.success(f"Capítulo generado correctamente: {path}")
            st.code(str(path))
