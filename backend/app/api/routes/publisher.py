from fastapi import APIRouter
from app.schemas.publisher import ChapterRequest
from app.services.publisher_service import build_chapter_markdown

router = APIRouter()

@router.post("/chapter")
def create_chapter(payload: ChapterRequest):
    slug = payload.title.lower().replace(" ", "-")
    return {"filename": f"{slug}.md", "markdown": build_chapter_markdown(payload)}
