from app.config import settings
from app.schemas import AIRequest


def select_model(request: AIRequest) -> str:
    """Seleciona o modelo local adequado para a solicitação.

    O roteamento inicial mantém um único modelo carregado para evitar
    competição por VRAM em GPUs com 4 GB.
    """
    if request.intent == "code":
        return "qwen2.5-coder:3b"

    return settings.default_model


def requires_approval(request: AIRequest) -> bool:
    """Ações externas ou de escrita exigem aprovação humana."""
    return settings.approval_required and request.intent == "action"
