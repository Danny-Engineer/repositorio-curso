from fastapi import APIRouter
from app.schemas.ai import GenerateRequest
from app.services.ai_service import generate_content

router = APIRouter()

@router.post("/generate")
def generate(payload: GenerateRequest):
    return generate_content(payload.topic, payload.audience, payload.tone, payload.context)
