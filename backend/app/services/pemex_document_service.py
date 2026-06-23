from app.schemas.pemex_document import OficioAnalysisRequest, OficioResponseRequest
from app.services.ai_service import generate_content

def analyze_oficio(payload: OficioAnalysisRequest) -> dict:
    text = payload.raw_text.strip()

    # Versión inicial basada en reglas simples. En v5 se integrará OCR y RAG.
    possible_subject = text.split("\n")[0][:120] if text else "Sin asunto detectado"

    detected_actions = []
    keywords = {
        "solicita": "Solicitud",
        "requiere": "Requerimiento",
        "informa": "Informe",
        "auditoría": "Auditoría",
        "evidencia": "Evidencia",
        "contrato": "Contrato",
        "procedimiento": "Procedimiento",
        "calidad": "Calidad",
    }

    lower_text = text.lower()
    for key, value in keywords.items():
        if key in lower_text:
            detected_actions.append(value)

    return {
        "document_type": payload.document_type,
        "area": payload.area,
        "subject_detected": possible_subject,
        "detected_topics": detected_actions or ["General"],
        "recommended_next_steps": [
            "Validar destinatario y remitente.",
            "Identificar plazo de atención.",
            "Buscar antecedentes documentales.",
            "Preparar borrador de respuesta institucional.",
            "Revisar jurídicamente si el asunto implica responsabilidad normativa."
        ],
        "risk_level": "medio" if any(x in lower_text for x in ["auditoría", "incumplimiento", "contrato", "riesgo"]) else "bajo"
    }

def generate_oficio_response(payload: OficioResponseRequest) -> dict:
    context = f'''
Texto base del oficio recibido:
{payload.raw_text}

Instrucción del usuario:
{payload.instruction}

Área emisora:
{payload.sender_area}

Destinatario:
{payload.recipient}

Firmante:
{payload.signer}
'''
    result = generate_content(
        topic="Respuesta institucional a oficio PEMEX",
        audience="personal administrativo y técnico de PEMEX",
        tone=payload.tone,
        context=context
    )

    fallback = f'''# Borrador de respuesta institucional

**Para:** {payload.recipient}  
**De:** {payload.sender_area}  
**Asunto:** Atención a solicitud recibida  

En atención al oficio de referencia, y con fundamento en la información disponible, se informa que esta área realizó la revisión preliminar del asunto planteado.

Derivado del análisis, se identifican los siguientes puntos de atención:

1. Validar los antecedentes documentales relacionados.
2. Verificar la competencia del área responsable.
3. Integrar la evidencia soporte disponible.
4. Emitir respuesta formal conforme al procedimiento aplicable.

Sin otro particular, se reitera la disposición para continuar con la atención correspondiente.

Atentamente,  

{payload.signer}
'''

    content = result.get("content") or fallback
    return {
        "provider": result.get("provider"),
        "draft_markdown": content,
        "template": "oficio_respuesta_pemex"
    }
