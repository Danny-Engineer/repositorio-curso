import streamlit as st
from ia.prompt_engine import build_structured_markdown
from config.settings import OUTPUT

def render_ia_assistant():
    st.header("🤖 IA Assistant")
    st.caption("Generador local simulado. En la siguiente versión se conectará a OpenAI/Claude.")

    topic = st.text_input("Tema a generar", "IA aplicada a Recursos Humanos")
    audience = st.text_input("Audiencia", "personal de Recursos Humanos y Gestión de Calidad")
    tone = st.selectbox("Tono", ["profesional", "ejecutivo", "académico", "institucional PEMEX"])
    depth = st.selectbox("Profundidad", ["introductoria", "intermedia", "avanzada"])

    if st.button("✨ Generar contenido"):
        content = build_structured_markdown(topic, audience, tone, depth)
        st.session_state["ia_content"] = content

    content = st.session_state.get("ia_content", "")
    if content:
        st.subheader("Resultado")
        edited = st.text_area("Contenido generado", content, height=500)
        st.markdown("### Vista previa")
        st.markdown(edited)

        if st.button("💾 Guardar en output"):
            OUTPUT.mkdir(parents=True, exist_ok=True)
            path = OUTPUT / "contenido_generado_ia.md"
            path.write_text(edited, encoding="utf-8")
            st.success(f"Guardado: {path}")
