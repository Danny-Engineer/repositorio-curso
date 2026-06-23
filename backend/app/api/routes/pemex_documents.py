from fastapi import APIRouter
from app.schemas.pemex_document import OficioAnalysisRequest, OficioResponseRequest
from app.services.pemex_document_service import analyze_oficio, generate_oficio_response

router = APIRouter()

@router.post("/analyze")
def analyze_document(payload: OficioAnalysisRequest):
    return analyze_oficio(payload)

@router.post("/generate-response")
def generate_response(payload: OficioResponseRequest):
    return generate_oficio_response(payload)
