"""Conservative privacy policy for YBY cloud providers."""

from dataclasses import dataclass
from enum import StrEnum


class DataClass(StrEnum):
    PUBLIC = "public"
    INTERNAL = "internal"
    SENSITIVE = "sensitive"
    RESTRICTED = "restricted"


@dataclass(frozen=True)
class PrivacyRequest:
    text: str
    data_class: DataClass = DataClass.INTERNAL
    cloud_consent: bool = False
    allow_sanitization: bool = True


class PrivacyPolicy:
    """Decides whether a request may reach a cloud provider."""

    _sensitive_fields = ("name", "location", "address", "email", "phone", "financial", "biometric")

    def classify(self, text: str) -> DataClass:
        lowered = text.lower()
        if any(token in lowered for token in ("senha", "token", "api key", "chave privada", "biometria")):
            return DataClass.RESTRICTED
        if any(token in lowered for token in ("nome", "endereço", "localização", "email", "telefone", "financeiro")):
            return DataClass.SENSITIVE
        if any(token in lowered for token in ("yby", "firmware", "telemetria", "arquitetura")):
            return DataClass.INTERNAL
        return DataClass.PUBLIC

    def authorize_cloud(self, request: PrivacyRequest) -> bool:
        if request.data_class in {DataClass.SENSITIVE, DataClass.RESTRICTED}:
            return False
        return request.cloud_consent

    def sanitize(self, text: str) -> str:
        sanitized = text
        for field in self._sensitive_fields:
            sanitized = sanitized.replace(field, "[REDACTED]")
        return sanitized

    def prepare_cloud_request(self, request: PrivacyRequest) -> tuple[bool, str, str]:
        if not self.authorize_cloud(request):
            return False, request.text, "cloud_not_authorized"
        if request.allow_sanitization:
            return True, self.sanitize(request.text), "authorized_sanitized"
        return True, request.text, "authorized_raw"
