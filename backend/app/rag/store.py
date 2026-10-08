from typing import Any

from qdrant_client import AsyncQdrantClient
from qdrant_client.models import Distance, VectorParams

from app.rag.config import rag_settings


class VectorStore:
    def __init__(self) -> None:
        self.client = AsyncQdrantClient(url=rag_settings.qdrant_url)

    async def ensure_collection(self, vector_size: int) -> None:
        collections = await self.client.get_collections()
        names = {collection.name for collection in collections.collections}

        if rag_settings.collection_name not in names:
            await self.client.create_collection(
                collection_name=rag_settings.collection_name,
                vectors_config=VectorParams(
                    size=vector_size,
                    distance=Distance.COSINE,
                ),
            )

    async def upsert_chunks(
        self,
        document_id: str,
        chunks: list[str],
        embeddings: list[list[float]],
        metadata: dict[str, Any],
    ) -> int:
        await self.ensure_collection(len(embeddings[0]))

        points = []

        for index, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            points.append(
                {
                    "id": f"{document_id}-{index}",
                    "vector": embedding,
                    "payload": {**metadata, "text": chunk, "chunk_index": index},
                }
            )

        await self.client.upsert(
            collection_name=rag_settings.collection_name,
            points=points,
        )

        return len(points)

    async def search(
        self,
        query_embedding: list[float],
        top_k: int,
    ) -> list[dict[str, Any]]:
        results = await self.client.query_points(
            collection_name=rag_settings.collection_name,
            query=query_embedding,
            limit=top_k,
            with_payload=True,
        )

        return [
            {
                "score": point.score,
                **point.payload,
            }
            for point in results.points
        ]
