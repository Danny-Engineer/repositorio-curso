from fastapi import APIRouter
from app.core.config import settings
from app.services.system_service import get_system_metrics

router = APIRouter()

@router.get("/status")
def system_status():
    return {
        "backend": "active",
        "ai_provider": settings.AI_PROVIDER,
        "openai_configured": bool(settings.OPENAI_API_KEY),
        "claude_configured": bool(settings.ANTHROPIC_API_KEY),
        "modules": ["Publisher", "AI Studio", "Knowledge Hub", "PEMEX Suite", "Motor Documental", "Learning", "Automation"]
    }

@router.get("/metrics")
def system_metrics():
    return get_system_metrics()
