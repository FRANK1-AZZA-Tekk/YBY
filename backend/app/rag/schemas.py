from pydantic import BaseModel, Field


class IngestRequest(BaseModel):
    title: str = Field(min_length=1, max_length=300)
    content: str = Field(min_length=1)
    project: str = "general"
    tags: list[str] = []
    source: str | None = None


class IngestResponse(BaseModel):
    document_id: str
    chunks_indexed: int
    collection: str


class RetrieveRequest(BaseModel):
    query: str = Field(min_length=1, max_length=2000)
    top_k: int = 4


class RetrievedChunk(BaseModel):
    text: str
    score: float
    title: str
    project: str
    tags: list[str]
    source: str | None = None


class RetrieveResponse(BaseModel):
    query: str
    chunks: list[RetrievedChunk]
