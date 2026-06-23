from datetime import datetime
from app.schemas.publisher import ChapterRequest

def build_chapter_markdown(payload: ChapterRequest) -> str:
    objectives = "\n".join([f"- {item}" for item in payload.objectives])
    competencies = "\n".join([f"- {item}" for item in payload.competencies])

    return f'''---
title: "{payload.title}"
author: "{payload.author}"
module: "{payload.module}"
level: "{payload.level}"
duration: "{payload.duration}"
created: "{datetime.utcnow().date()}"
---

# {payload.title}

## Resumen ejecutivo

{payload.summary}

## Objetivos de aprendizaje

{objectives}

## Competencias

{competencies}

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

## Laboratorio

Pendiente de desarrollar.

## Prompt Lab

```text
Actúa como experto en inteligencia artificial empresarial y desarrolla el tema: {payload.title}
```

## Buenas prácticas

- Validar el contenido generado.
- Proteger datos sensibles.
- Mantener revisión humana.

## Bibliografía

Pendiente.
'''
