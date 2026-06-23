from pathlib import Path
from config.settings import PROMPTS

DEFAULT_PROMPTS = {
    "capitulo_empresarial": """Actúa como consultor experto en inteligencia artificial empresarial.
Desarrolla un capítulo profesional sobre: {tema}.
Incluye resumen ejecutivo, objetivos, desarrollo conceptual, caso práctico, laboratorio, buenas prácticas y errores comunes.""",
    "rh": """Actúa como experto en Recursos Humanos e Inteligencia Artificial.
Propón aplicaciones prácticas, riesgos, métricas e implementación para el tema: {tema}.""",
    "calidad": """Actúa como auditor líder ISO 9001 y experto en IA.
Desarrolla un enfoque aplicable a gestión de calidad para el tema: {tema}.""",
    "pemex": """Actúa como consultor de transformación digital para procesos corporativos del sector energético.
Redacta con tono institucional y práctico el tema: {tema}.""",
}

def ensure_prompt_library():
    PROMPTS.mkdir(parents=True, exist_ok=True)
    for name, content in DEFAULT_PROMPTS.items():
        path = PROMPTS / f"{name}.md"
        if not path.exists():
            path.write_text(content, encoding="utf-8")

def list_prompts():
    ensure_prompt_library()
    return sorted(PROMPTS.glob("*.md"))

def read_prompt(path: Path) -> str:
    return path.read_text(encoding="utf-8")
