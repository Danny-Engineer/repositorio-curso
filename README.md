# Logística IA Lab Suite - Enterprise v4

Versión empresarial con primer módulo funcional de **Motor Documental PEMEX**.

## Novedades v4

- Backend FastAPI.
- Frontend React.
- IA configurable: local, OpenAI o Claude.
- Publisher API.
- AI Studio.
- PEMEX Suite inicial.
- Motor Documental PEMEX:
  - análisis de oficio,
  - extracción simulada de datos,
  - generación de borrador de respuesta institucional,
  - plantilla base de oficio.

## Inicio rápido

1. Copia `.env.example` como `.env`.
2. Ejecuta:

```powershell
docker compose up --build
```

Backend:
http://localhost:8000/docs

Frontend:
http://localhost:5173
