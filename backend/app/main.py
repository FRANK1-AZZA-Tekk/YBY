from fastapi import FastAPI

from app.config import settings
from app.routers import ai, health

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Hub local do ecossistema YBY.",
)

app.include_router(health.router)
app.include_router(ai.router)


@app.get("/")
async def root() -> dict:
    return {
        "name": settings.app_name,
        "docs": "/docs",
        "health": "/health",
    }
