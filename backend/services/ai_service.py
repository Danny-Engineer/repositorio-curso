from app.core.config import settings

def generate_content(topic: str, audience: str, tone: str, context: str | None = None) -> dict:
    content = f'''# {topic}

## Resumen ejecutivo
Contenido generado en modo local simulado para **{audience}**, con tono **{tone}**.

## Contexto
{context or "Sin contexto adicional."}

## Aplicaciones
- Recursos Humanos.
- Gestión de Calidad.
- Sector energético.
- Automatización documental.
- RAG corporativo.
- Generación de oficios.

## Conclusión
Modo local activo. Configura OpenAI o Claude en `.env` para generación real.
'''
    return {"provider": settings.AI_PROVIDER, "content": content}
