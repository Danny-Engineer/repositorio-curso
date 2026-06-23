import platform
import shutil
import psutil
from app.core.config import settings

def get_system_metrics() -> dict:
    disk = shutil.disk_usage("/")
    memory = psutil.virtual_memory()
    return {
        "system": {"os": platform.system(), "release": platform.release(), "architecture": platform.machine(), "python": platform.python_version()},
        "resources": {
            "cpu_percent": psutil.cpu_percent(interval=0.2),
            "memory_percent": memory.percent,
            "memory_total_gb": round(memory.total / (1024 ** 3), 2),
            "memory_available_gb": round(memory.available / (1024 ** 3), 2),
            "disk_percent": round((disk.used / disk.total) * 100, 2),
            "disk_total_gb": round(disk.total / (1024 ** 3), 2),
            "disk_free_gb": round(disk.free / (1024 ** 3), 2),
        },
        "services": {"fastapi": "active", "postgresql": "active", "frontend": "active", "docker": "active", "mkdocs": "configured", "rag": "pending", "n8n": "pending", "ollama": "pending"},
        "ai": {"provider": settings.AI_PROVIDER, "openai_configured": bool(settings.OPENAI_API_KEY), "claude_configured": bool(settings.ANTHROPIC_API_KEY), "openai_model": settings.OPENAI_MODEL, "claude_model": settings.ANTHROPIC_MODEL},
    }
