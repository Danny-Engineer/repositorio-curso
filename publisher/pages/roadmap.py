import streamlit as st

def render_roadmap():
    st.header("🧭 Roadmap del Publisher")

    st.markdown("""
## Versión 1
- Dashboard
- Generador de capítulos
- Exportación DOCX
- GitHub básico
- MkDocs básico

## Versión 2
- Editor Markdown con vista previa
- Git log / pull / push
- Exportador mejorado

## Versión 3
- IA Assistant simulado
- Biblioteca de prompts
- Roadmap
- Preparación para OpenAI/Claude

## Próximas versiones
- OpenAI API
- Claude API
- RAG documental
- Generador de imágenes
- Exportación PDF/PPTX
- Motor documental PEMEX
""")
