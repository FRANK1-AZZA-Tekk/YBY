from fastapi import APIRouter

from app.rag.schemas import (
    IngestRequest,
    IngestResponse,
    RetrieveRequest,
    RetrieveResponse,
)
from app.rag.service import rag_service

router = APIRouter(prefix="/rag", tags=["rag"])


@router.post("/ingest", response_model=IngestResponse)
async def ingest(request: IngestRequest) -> IngestResponse:
    return await rag_service.ingest(request)


@router.post("/retrieve", response_model=RetrieveResponse)
async def retrieve(request: RetrieveRequest) -> RetrieveResponse:
    return await rag_service.retrieve(request)
