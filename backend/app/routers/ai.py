from fastapi import APIRouter, HTTPException

import httpx

from app.config import settings
from app.schemas import AIRequest, AIResponse
from app.services.ai_router import requires_approval, select_model

router = APIRouter(prefix="/ai", tags=["ai"])


@router.post("/chat", response_model=AIResponse)
async def chat(request: AIRequest) -> AIResponse:
    model = select_model(request)
    approval_required = requires_approval(request)

    if approval_required:
        raise HTTPException(
            status_code=403,
            detail="Ação sensível detectada. Aprovação humana é obrigatória.",
        )

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": request.prompt}],
        "stream": False,
    }

    try:
        async with httpx.AsyncClient(timeout=120) as client:
            response = await client.post(
                f"{settings.ollama_base_url}/api/chat", json=payload
            )
            response.raise_for_status()
            data = response.json()
    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Não foi possível acionar o Ollama: {exc}",
        ) from exc

    answer = data.get("message", {}).get("content", "")

    return AIResponse(
        answer=answer,
        model=model,
        intent=request.intent,
        approval_required=False,
    )
