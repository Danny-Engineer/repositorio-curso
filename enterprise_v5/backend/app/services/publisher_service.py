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

## Desarrollo
Pendiente de desarrollar.
'''
