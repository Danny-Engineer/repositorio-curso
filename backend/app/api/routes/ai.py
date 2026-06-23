from fastapi import APIRouter
from app.schemas.ai import GenerateRequest, TestProviderRequest
from app.services.ai_service import generate_content, available_providers, test_provider

router = APIRouter()

@router.get("/providers")
def providers():
    return available_providers()

@router.post("/generate")
def generate(payload: GenerateRequest):
    return generate_content(payload.topic, payload.audience, payload.tone, payload.context, payload.provider, payload.model)

@router.post("/test")
def test(payload: TestProviderRequest):
    return test_provider(payload.provider, payload.model)
