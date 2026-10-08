from app.rag.config import rag_settings


def chunk_text(text: str) -> list[str]:
    """Divide texto preservando parágrafos e aplicando overlap."""
    normalized = "\n\n".join(
        paragraph.strip() for paragraph in text.split("\n\n") if paragraph.strip()
    )

    if not normalized:
        return []

    size = rag_settings.chunk_size
    overlap = rag_settings.chunk_overlap
    chunks = []
    start = 0

    while start < len(normalized):
        end = min(start + size, len(normalized))
        chunk = normalized[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end == len(normalized):
            break

        start = max(end - overlap, start + 1)

    return chunks
