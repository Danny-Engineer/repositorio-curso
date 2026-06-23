from pathlib import Path
from datetime import datetime
from config.settings import DOCS
from utils.helpers import slugify

MODULES = [
    "00-editorial",
    "01-fundamentos-ia",
    "02-recursos-humanos",
    "03-gestion-calidad",
    "04-automatizacion",
    "05-rag",
    "06-agentes",
    "07-sector-energetico",
    "08-laboratorios",
    "09-proyecto-final",
]

def list_markdown_files():
    return sorted(DOCS.rglob("*.md"))

def read_markdown(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def save_markdown(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")

def create_chapter(module, number, title, author, duration, level, objectives, competencies, summary) -> Path:
    slug = slugify(title)
    folder = DOCS / module
    folder.mkdir(parents=True, exist_ok=True)
    file_path = folder / f"{number}-{slug}.md"

    obj_md = "\n".join(f"- {line.strip()}" for line in objectives.splitlines() if line.strip())
    comp_md = "\n".join(f"- {line.strip()}" for line in competencies.splitlines() if line.strip())

    content = f"""---
title: "{title}"
author: "{author}"
module: "{module}"
duration: "{duration}"
level: "{level}"
created: "{datetime.now().strftime("%Y-%m-%d")}"
---

# {title}

## Resumen ejecutivo

{summary}

## Objetivos de aprendizaje

{obj_md}

## Competencias

{comp_md}

## Introducción

Pendiente de desarrollar.

## Desarrollo conceptual

Pendiente de desarrollar.

## Aplicación en Recursos Humanos

Pendiente de desarrollar.

## Aplicación en Gestión de Calidad

Pendiente de desarrollar.

## Caso práctico

Pendiente de desarrollar.

## Laboratorio guiado

Pendiente de desarrollar.

## Prompt Lab

```text
Actúa como consultor experto en inteligencia artificial empresarial y desarrolla este tema: {title}
```

## Buenas prácticas

- Validar la información generada por IA.
- Proteger datos sensibles.
- Documentar criterios de uso.

## Errores comunes

- Usar IA sin contexto.
- Copiar respuestas sin revisión.
- No validar fuentes.

## Actividad práctica

Pendiente de desarrollar.

## Autoevaluación

1. ¿Cuál es el objetivo principal del capítulo?
2. ¿Qué aplicación tiene en Recursos Humanos?
3. ¿Qué aplicación tiene en Gestión de Calidad?

## Bibliografía

Pendiente.
"""
    file_path.write_text(content, encoding="utf-8")
    return file_path
