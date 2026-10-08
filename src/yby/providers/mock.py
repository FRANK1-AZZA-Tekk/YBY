"""Deterministic provider used for tests and offline fallback."""

from .base import ProviderRequest, ProviderResult


class MockProvider:
    name = "mock"

    def __init__(self, model: str = "mock-v1") -> None:
        self.model = model

    def generate(self, request: ProviderRequest) -> ProviderResult:
        output = {"answer": f"Resposta simulada para: {request.text}"}
        return ProviderResult(
            provider=self.name,
            model=self.model,
            status="success",
            output=output,
            sensitive_data_sent=False,
        )
