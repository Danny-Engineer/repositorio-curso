def build_structured_markdown(topic: str, audience: str, tone: str, depth: str) -> str:
    """Generador local simulado. En la siguiente versión se conectará a OpenAI/Claude."""
    return f"""# {topic}

## Resumen ejecutivo

Este documento presenta una propuesta inicial sobre **{topic}**, dirigida a **{audience}**, con un tono **{tone}** y nivel de profundidad **{depth}**.

## Objetivos

- Comprender los fundamentos del tema.
- Identificar aplicaciones empresariales.
- Diseñar un caso práctico aplicable.
- Reconocer riesgos y buenas prácticas.

## Desarrollo conceptual

La inteligencia artificial permite rediseñar procesos empresariales mediante automatización, análisis de datos y generación asistida de contenido. En este contexto, el tema **{topic}** debe abordarse desde una perspectiva práctica, ética y orientada a resultados.

## Caso práctico

Una organización requiere mejorar un proceso documental repetitivo. El equipo diseña un flujo donde la IA apoya la lectura de documentos, la extracción de datos, la generación de borradores y la validación humana final.

## Laboratorio guiado

1. Definir el proceso objetivo.
2. Identificar entradas y salidas.
3. Crear un prompt base.
4. Ejecutar una prueba.
5. Validar resultados.
6. Documentar hallazgos.

## Prompt Lab

```text
Actúa como experto en IA empresarial. Desarrolla una propuesta aplicada sobre {topic} para {audience}.
```

## Buenas prácticas

- Mantener revisión humana.
- Evitar datos sensibles.
- Documentar criterios.
- Medir resultados.

## Errores comunes

- Automatizar sin entender el proceso.
- Confiar ciegamente en la IA.
- No validar fuentes.
- No capacitar usuarios.

## Conclusión

El tema **{topic}** puede generar valor si se implementa con metodología, gobierno y enfoque práctico.
"""
