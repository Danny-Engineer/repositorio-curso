from pydantic import BaseModel

class OficioAnalysisRequest(BaseModel):
    raw_text: str
    area: str = "Servicios Logísticos"
    document_type: str = "Oficio"

class OficioResponseRequest(BaseModel):
    raw_text: str
    instruction: str = "Elabora una respuesta institucional."
    sender_area: str = "Área de Especialidad de Servicios Logísticos Terrestres"
    recipient: str = "Área solicitante"
    signer: str = "Daniel Melchor Pérez"
    tone: str = "institucional"
