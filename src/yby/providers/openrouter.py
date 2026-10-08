"""Explicit OpenRouter provider for non-sensitive cloud tasks."""

import json
import os
import time
from typing import Any

from openai import OpenAI

from .base import ProviderRequest, ProviderResult


class OpenRouterProvider:
    name = "openrouter"

    def __init__(self, model: str | None = None, api_key: str | None = None) -> None:
        self.model = model or os.getenv("YBY_OPENROUTER_MODEL", "openai/gpt-6-luna")
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        self.base_url = os.getenv("YBY_OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
        self.client = OpenAI(api_key=self.api_key or "missing-key", base_url=self.base_url)

    def generate(self, request: ProviderRequest) -> ProviderResult:
        if not self.api_key:
            return ProviderResult(
                provider=self.name,
                model=self.model,
                status="blocked",
                output=None,
                error_code="missing_openrouter_api_key",
                sensitive_data_sent=False,
            )

        messages: list[dict[str, str]] = []
        if request.system:
            messages.append({"role": "system", "content": request.system})
        messages.append({"role": "user", "content": request.text})
        kwargs: dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "extra_body": {"provider": {"require_parameters": True}},
        }
        if request.response_schema:
            kwargs["response_format"] = {
                "type": "json_schema",
                "json_schema": {"name": "yby_response", "strict": True, "schema": request.response_schema},
            }

        started = time.perf_counter()
        try:
            response = self.client.chat.completions.create(**kwargs)
            content = response.choices[0].message.content or ""
            output: Any = json.loads(content) if request.response_schema else content
            return ProviderResult(
                provider=self.name,
                model=self.model,
                status="success",
                output=output,
                latency_ms=(time.perf_counter() - started) * 1000,
                sensitive_data_sent=False,
            )
        except (json.JSONDecodeError, IndexError, KeyError) as exc:
            return ProviderResult(
                provider=self.name,
                model=self.model,
                status="error",
                output=None,
                latency_ms=(time.perf_counter() - started) * 1000,
                error_code=type(exc).__name__,
                sensitive_data_sent=True,
            )
        except Exception as exc:
            return ProviderResult(
                provider=self.name,
                model=self.model,
                status="error",
                output=None,
                latency_ms=(time.perf_counter() - started) * 1000,
                error_code=type(exc).__name__,
                sensitive_data_sent=True,
            )
