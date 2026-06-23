from pydantic import BaseModel, Field

class ChapterRequest(BaseModel):
    title: str
    module: str = "01-fundamentos-ia"
    author: str = "Daniel Melchor Pérez"
    level: str = "Ejecutivo"
    duration: str = "60 minutos"
    summary: str = "Pendiente de desarrollar."
    objectives: list[str] = Field(default_factory=lambda: [
        "Comprender el tema.",
        "Aplicarlo al contexto empresarial.",
        "Diseñar un caso práctico."
    ])
    competencies: list[str] = Field(default_factory=lambda: [
        "Pensamiento crítico.",
        "Uso de IA.",
        "Automatización documental."
    ])
