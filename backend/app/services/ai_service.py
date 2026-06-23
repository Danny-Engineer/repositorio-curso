from openai import OpenAI
from anthropic import Anthropic
from app.core.config import settings

SYSTEM_PROMPT = """Eres un consultor experto en inteligencia artificial empresarial,
recursos humanos, gestión de calidad, documentación técnica, sector energético,
PEMEX y transformación digital. Redacta en español con estilo profesional,
claro, institucional y aplicable."""

def _build_user_prompt(topic: str, audience: str, tone: str, context: str | None = None) -> str:
    context_block = f"\nContexto adicional:\n{context}\n" if context else ""
    return f"""Desarrolla contenido profesional sobre: {topic}

Audiencia: {audience}
Tono: {tone}

Incluye:
- Resumen ejecutivo.
- Objetivos.
- Desarrollo conceptual.
- Aplicaciones empresariales.
- Caso práctico.
- Laboratorio guiado.
- Buenas prácticas.
- Errores comunes.
- Conclusión.
{context_block}
"""

def generate_local(topic: str, audience: str, tone: str, context: str | None = None) -> str:
    context_block = f"\n## Contexto proporcionado\n\n{context}\n" if context else ""
    return f'''# {topic}

## Resumen ejecutivo

Contenido generado en modo local simulado para **{audience}**, con tono **{tone}**.

{context_block}

## Desarrollo

Esta versión está lista para integrarse con OpenAI o Claude.

## Aplicaciones empresariales

- Recursos Humanos.
- Gestión de Calidad.
- Sector energético.
- Automatización documental.
- RAG corporativo.
- Generación de oficios.

## Conclusión

Modo local activo. Configura OpenAI o Claude en `.env` para generación real.
'''

def generate_openai(topic: str, audience: str, tone: str, context: str | None = None) -> str:
    if not settings.OPENAI_API_KEY:
        return generate_local(topic, audience, tone, "OPENAI_API_KEY no configurada.")

    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=settings.OPENAI_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": _build_user_prompt(topic, audience, tone, context)}
        ],
        temperature=0.4,
    )
    return response.choices[0].message.content

def generate_claude(topic: str, audience: str, tone: str, context: str | None = None) -> str:
    if not settings.ANTHROPIC_API_KEY:
        return generate_local(topic, audience, tone, "ANTHROPIC_API_KEY no configurada.")

    client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
    msg = client.messages.create(
        model=settings.ANTHROPIC_MODEL,
        max_tokens=3000,
        temperature=0.4,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": _build_user_prompt(topic, audience, tone, context)}
        ]
    )
    return msg.content[0].text

def generate_content(topic: str, audience: str, tone: str, context: str | None = None) -> dict:
    provider = settings.AI_PROVIDER.lower()

    if provider == "openai":
        content = generate_openai(topic, audience, tone, context)
    elif provider == "claude":
        content = generate_claude(topic, audience, tone, context)
    else:
        content = generate_local(topic, audience, tone, context)
        provider = "local"

    return {"provider": provider, "content": content}
