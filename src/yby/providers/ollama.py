"""Local Ollama provider for YBY."""

import json
import os
import time
from typing import Any

import ollama

from .base import ProviderRequest, ProviderResult


class OllamaProvider:
    """Calls the local Ollama API without sending data to the cloud."""

    name = "ollama"

    def __init__(self, model: str | None = None, host: str | None = None) -> None:
        self.model = model or os.getenv("YBY_OLLAMA_MODEL", "llama3.2:3b")
        self.host = host or os.getenv("YBY_OLLAMA_BASE_URL", "http://localhost:11434")
        self.client = ollama.Client(host=self.host)

    def generate(self, request: ProviderRequest) -> ProviderResult:
        messages = []
        if request.system:
            messages.append({"role": "system", "content": request.system})
        messages.append({"role": "user", "content": request.text})
        started = time.perf_counter()
        try:
            response = self.client.chat(
                model=self.model,
                messages=messages,
                stream=False,
                format=request.response_schema or "json",
            )
            content = response["message"]["content"]
            output: Any
            if request.response_schema:
                output = json.loads(content)
            else:
                output = content
            return ProviderResult(
                provider=self.name,
                model=self.model,
                status="success",
                output=output,
                latency_ms=(time.perf_counter() - started) * 1000,
            )
        except (ollama.ResponseError, json.JSONDecodeError, KeyError) as exc:
            return ProviderResult(
                provider=self.name,
                model=self.model,
                status="error",
                output=None,
                latency_ms=(time.perf_counter() - started) * 1000,
                error_code=type(exc).__name__,
            )
        except Exception:
            return ProviderResult(
                provider=self.name,
                model=self.model,
                status="error",
                output=None,
                latency_ms=(time.perf_counter() - started) * 1000,
                error_code="ollama_unavailable",
            )
