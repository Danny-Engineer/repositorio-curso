from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import health, system, ai, publisher, pemex_documents

app = FastAPI(
    title="Logística IA Lab Suite API",
    version="4.0.0",
    description="API empresarial para Publisher, IA, RAG y Motor Documental PEMEX."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api/health", tags=["health"])
app.include_router(system.router, prefix="/api/system", tags=["system"])
app.include_router(ai.router, prefix="/api/ai", tags=["ai"])
app.include_router(publisher.router, prefix="/api/publisher", tags=["publisher"])
app.include_router(pemex_documents.router, prefix="/api/pemex/documents", tags=["pemex-documents"])
