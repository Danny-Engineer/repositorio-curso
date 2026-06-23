import streamlit as st
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ASSETS = ROOT / "assets"
PROMPTS = ROOT / "prompts"
OUTPUT = ROOT / "output"

st.set_page_config(
    page_title="Logística IA Lab Publisher",
    page_icon="📚",
    layout="wide"
)

def count_files(folder: Path, pattern: str):
    return len(list(folder.rglob(pattern))) if folder.exists() else 0

def run_command(command):
    try:
        result = subprocess.run(
            command,
            cwd=ROOT,
            shell=True,
            capture_output=True,
            text=True
        )
        return result.stdout.strip() or result.stderr.strip()
    except Exception as e:
        return str(e)

st.sidebar.title("📚 Menú")
option = st.sidebar.selectbox(
    "Selecciona una opción",
    [
        "Dashboard",
        "Capítulos",
        "Exportar",
        "GitHub",
        "MkDocs",
        "Configuración"
    ]
)

st.title("📚 Logística IA Lab Publisher")
st.caption("Suite editorial para cursos, manuales, documentación técnica e IA empresarial")

if option == "Dashboard":
    st.header("📊 Dashboard Ejecutivo")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Archivos Markdown", count_files(DOCS, "*.md"))
    col2.metric("Imágenes", count_files(ASSETS, "*.png") + count_files(ASSETS, "*.jpg") + count_files(ASSETS, "*.svg"))
    col3.metric("Prompts", count_files(PROMPTS, "*.md") + count_files(PROMPTS, "*.txt"))
    col4.metric("Documentos generados", count_files(OUTPUT, "*.*"))

    st.divider()

    st.subheader("Estado del entorno")

    col5, col6, col7 = st.columns(3)

    col5.success("Python activo")
    col6.success("Streamlit activo")
    col7.success("Repositorio activo")

    st.divider()

    st.subheader("Acciones rápidas")

    c1, c2, c3, c4 = st.columns(4)

    if c1.button("➕ Nuevo capítulo"):
        st.session_state["go_to"] = "Capítulos"
        st.info("Ve al menú lateral y selecciona Capítulos.")

    if c2.button("🌐 Ejecutar MkDocs"):
        output = run_command("mkdocs build")
        st.code(output)

    if c3.button("☁ Git status"):
        output = run_command("git status")
        st.code(output)

    if c4.button("📦 Git push"):
        output = run_command("git add . && git commit -m \"Actualización desde Publisher\" && git push")
        st.code(output)

elif option == "Capítulos":
    st.header("📖 Crear nuevo capítulo")

    module = st.selectbox(
        "Módulo",
        [
            "01-fundamentos-ia",
            "02-recursos-humanos",
            "03-gestion-calidad",
            "04-automatizacion",
            "05-rag",
            "06-agentes",
            "07-sector-energetico",
            "08-laboratorios",
            "09-proyecto-final"
        ]
    )

    number = st.text_input("Número", "02")
    title = st.text_input("Título del capítulo")
    author = st.text_input("Autor", "Daniel Melchor Pérez")

    if st.button("Crear capítulo"):
        if not title:
            st.error("Escribe un título.")
        else:
            slug = title.lower()
            for a, b in {
                "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ñ": "n"
            }.items():
                slug = slug.replace(a, b)
            slug = "-".join(slug.split())

            folder = DOCS / module
            folder.mkdir(parents=True, exist_ok=True)

            file_path = folder / f"{number}-{slug}.md"

            content = f"""---
title: "{title}"
author: "{author}"
module: "{module}"
---

# {title}

## Resumen ejecutivo

Pendiente de desarrollar.

## Objetivos de aprendizaje

- Objetivo 1.
- Objetivo 2.
- Objetivo 3.

## Competencias

- Competencia técnica.
- Competencia analítica.
- Competencia aplicada.

## Desarrollo

Pendiente de desarrollar.

## Caso práctico

Pendiente de desarrollar.

## Laboratorio

Pendiente de desarrollar.

## Prompt Lab

```text
Actúa como experto en inteligencia artificial empresarial.