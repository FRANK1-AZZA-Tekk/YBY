from typing import Literal

from pydantic import BaseModel, Field


class AIRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=8000)
    intent: Literal[
        "chat", "research", "hardware", "code", "memory", "action"
    ] = "chat"
    use_rag: bool = False


class AISource(BaseModel):
    title: str
    url: str | None = None
    snippet: str | None = None


class AIResponse(BaseModel):
    answer: str
    model: str
    intent: str
    sources: list[AISource] = []
    approval_required: bool = False
