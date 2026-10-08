"""Minimal local-first router for the YBY foundation."""

from yby.core.models import Intent, RouteDecision


class HybridRouter:
    """Select a route without making external calls."""

    def decide(self, intent: Intent) -> RouteDecision:
        if intent.requires_hardware:
            return RouteDecision("tool", "hardware access must go through a controlled tool")
        if intent.sensitive:
            return RouteDecision("local", "sensitive data stays local")
        if intent.complexity == "complex":
            return RouteDecision("openrouter", "complex task may benefit from a cloud model")
        return RouteDecision("local", "simple task uses the local-first path")
