from openai import OpenAI
from anthropic import Anthropic
from app.core.config import settings

SYSTEM_PROMPT = """Eres un consultor experto en inteligencia artificial empresarial,
recursos humanos, gestión de calidad, documentación técnica, sector energético,
PEMEX y transformación digital. Redacta en español con estilo profesional,
claro, institucional y aplicable."""

def available_providers() -> dict:
    return {
        "default_provider": settings.AI_PROVIDER,
        "providers": [
            {"id": "local", "name": "Local Simulado", "configured": True, "models": ["local-simulated"]},
            {"id": "openai", "name": "OpenAI", "configured": bool(settings.OPENAI_API_KEY), "models": [settings.OPENAI_MODEL, "gpt-4o-mini", "gpt-4o"]},
            {"id": "claude", "name": "Claude", "configured": bool(settings.ANTHROPIC_API_KEY), "models": [settings.ANTHROPIC_MODEL, "claude-3-5-sonnet-latest"]}
        ]
    }

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
    return f"""# {topic}

## Resumen ejecutivo

Contenido generado en modo local simulado para **{audience}**, con tono **{tone}**.

## Contexto

{context or "Sin contexto adicional."}

## Objetivos

- Comprender el tema.
- Identificar aplicaciones empresariales.
- Aplicar el conocimiento en un caso práctico.
- Documentar criterios de uso.

## Desarrollo conceptual

Este módulo valida el flujo completo de AI Studio sin consumir tokens externos. Cuando configures `AI_PROVIDER=openai` o `AI_PROVIDER=claude`, el sistema usará el proveedor correspondiente.

## Aplicaciones empresariales

- Recursos Humanos.
- Gestión de Calidad.
- Sector energético.
- Automatización documental.
- RAG corporativo.
- Generación de oficios.

## Buenas prácticas

- Validar siempre el contenido generado.
- No incluir datos sensibles innecesarios.
- Mantener trazabilidad de fuentes.
- Documentar criterios de revisión.

## Conclusión

El AI Studio ya está preparado para proveedores reales mediante variables de entorno.
"""

def generate_openai(topic: str, audience: str, tone: str, context: str | None = None, model: str | None = None) -> str:
    if not settings.OPENAI_API_KEY:
        return generate_local(topic, audience, tone, "OPENAI_API_KEY no configurada.")
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=model or settings.OPENAI_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": _build_user_prompt(topic, audience, tone, context)}
        ],
        temperature=0.4,
    )
    return response.choices[0].message.content

def generate_claude(topic: str, audience: str, tone: str, context: str | None = None, model: str | None = None) -> str:
    if not settings.ANTHROPIC_API_KEY:
        return generate_local(topic, audience, tone, "ANTHROPIC_API_KEY no configurada.")
    client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
    msg = client.messages.create(
        model=model or settings.ANTHROPIC_MODEL,
        max_tokens=3500,
        temperature=0.4,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": _build_user_prompt(topic, audience, tone, context)}]
    )
    return msg.content[0].text

def generate_content(topic: str, audience: str, tone: str, context: str | None = None, provider: str | None = None, model: str | None = None) -> dict:
    selected_provider = (provider or settings.AI_PROVIDER or "local").lower()

    if selected_provider == "openai":
        content = generate_openai(topic, audience, tone, context, model)
    elif selected_provider == "claude":
        content = generate_claude(topic, audience, tone, context, model)
    else:
        selected_provider = "local"
        content = generate_local(topic, audience, tone, context)

    return {"provider": selected_provider, "model": model, "content": content}

def test_provider(provider: str, model: str | None = None) -> dict:
    result = generate_content(
        topic="Prueba de conexión IA",
        audience="usuario técnico",
        tone="breve",
        context="Responde con una confirmación breve.",
        provider=provider,
        model=model
    )
    return {"provider": result["provider"], "model": result.get("model"), "ok": True, "sample": result["content"][:500]}
