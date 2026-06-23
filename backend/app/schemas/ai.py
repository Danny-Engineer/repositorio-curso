from pydantic import BaseModel

class GenerateRequest(BaseModel):
    topic: str
    audience: str = "personal corporativo"
    tone: str = "profesional"
    context: str | None = None
    provider: str | None = None
    model: str | None = None

class TestProviderRequest(BaseModel):
    provider: str
    model: str | None = None
