from uuid import uuid4

from app.rag.chunking import chunk_text
from app.rag.config import rag_settings
from app.rag.embeddings import create_embedding
from app.rag.schemas import (
    IngestRequest,
    IngestResponse,
    RetrieveRequest,
    RetrieveResponse,
    RetrievedChunk,
)
from app.rag.store import VectorStore


class RAGService:
    def __init__(self) -> None:
        self.store = VectorStore()

    async def ingest(self, request: IngestRequest) -> IngestResponse:
        document_id = str(uuid4())
        chunks = chunk_text(request.content)

        if not chunks:
            return IngestResponse(
                document_id=document_id,
                chunks_indexed=0,
                collection=rag_settings.collection_name,
            )

        embeddings = [await create_embedding(chunk) for chunk in chunks]

        metadata = {
            "title": request.title,
            "project": request.project,
            "tags": request.tags,
            "source": request.source,
            "document_id": document_id,
        }

        indexed = await self.store.upsert_chunks(
            document_id=document_id,
            chunks=chunks,
            embeddings=embeddings,
            metadata=metadata,
        )

        return IngestResponse(
            document_id=document_id,
            chunks_indexed=indexed,
            collection=rag_settings.collection_name,
        )

    async def retrieve(self, request: RetrieveRequest) -> RetrieveResponse:
        query_embedding = await create_embedding(request.query)
        results = await self.store.search(
            query_embedding=query_embedding,
            top_k=request.top_k or rag_settings.top_k,
        )

        chunks = [
            RetrievedChunk(
                text=result.get("text", ""),
                score=float(result.get("score", 0.0)),
                title=result.get("title", "Documento"),
                project=result.get("project", "general"),
                tags=result.get("tags", []),
                source=result.get("source"),
            )
            for result in results
        ]

        return RetrieveResponse(query=request.query, chunks=chunks)


rag_service = RAGService()
