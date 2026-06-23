from app.schemas.pemex_document import OficioAnalysisRequest, OficioResponseRequest
from app.services.ai_service import generate_content

def analyze_oficio(payload: OficioAnalysisRequest) -> dict:
    text = payload.raw_text.strip()
    lower_text = text.lower()
    topics = []
    for key, value in {"solicita": "Solicitud", "auditoría": "Auditoría", "evidencia": "Evidencia", "contrato": "Contrato", "calidad": "Calidad"}.items():
        if key in lower_text:
            topics.append(value)
    return {
        "document_type": payload.document_type,
        "area": payload.area,
        "subject_detected": text.split("\n")[0][:120] if text else "Sin asunto detectado",
        "detected_topics": topics or ["General"],
        "risk_level": "medio" if any(x in lower_text for x in ["auditoría", "incumplimiento", "contrato", "riesgo"]) else "bajo",
        "recommended_next_steps": ["Validar remitente.", "Buscar antecedentes.", "Preparar respuesta institucional."]
    }

def generate_oficio_response(payload: OficioResponseRequest) -> dict:
    result = generate_content("Respuesta institucional a oficio PEMEX", "personal PEMEX", payload.tone, payload.raw_text)
    return {"provider": result.get("provider"), "draft_markdown": result.get("content"), "template": "oficio_respuesta_pemex"}
