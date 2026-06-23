from pydantic import BaseModel

class GenerateRequest(BaseModel):
    topic: str
    audience: str = "personal corporativo"
    tone: str = "profesional"
    context: str | None = None
