from typing import Any

import httpx

from app.rag.config import rag_settings


class EmbeddingError(RuntimeError):
    pass


async def create_embedding(text: str) -> list[float]:
    """Gera embeddings localmente usando o Ollama."""
    payload = {"model": rag_settings.embedding_model, "input": text}

    try:
        async with httpx.AsyncClient(timeout=120) as client:
            response = await client.post(
                f"{rag_settings.ollama_base_url}/api/embed", json=payload
            )
            response.raise_for_status()
            data: dict[str, Any] = response.json()
    except httpx.HTTPError as exc:
        raise EmbeddingError(f"Falha ao gerar embedding: {exc}") from exc

    embeddings = data.get("embeddings")

    if not embeddings or not embeddings[0]:
        raise EmbeddingError("O Ollama não retornou um embedding válido.")

    return embeddings[0]
