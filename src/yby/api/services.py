"""Application services for the first local YBY API."""

import json
from pathlib import Path

from jsonschema import Draft202012Validator

from yby.core.models import Intent
from yby.providers import ProviderRequest, ProviderRouter
from yby.router import HybridRouter

from .models import DeviceStatus, UIState


class DeviceService:
    """Provides simulated device data until real telemetry is integrated."""

    def status(self, device_id: str) -> DeviceStatus:
        return DeviceStatus(
            device_id=device_id,
            battery_percent=78,
            temperature_c=34.2,
            ble_connected=True,
            wifi_connected=False,
            power_mode="balanced",
            firmware="0.1.0-simulated",
            source="simulated",
        )


class IntentService:
    def __init__(self) -> None:
        self.router = HybridRouter()
        self.provider_router = ProviderRouter()
        self.device_service = DeviceService()
        schema_path = Path(__file__).parents[3] / "contracts" / "ui_state.schema.json"
        self.ui_validator = Draft202012Validator(json.loads(schema_path.read_text(encoding="utf-8")))

    def process(self, text: str, device_id: str) -> tuple[str, str, UIState]:
        intent = Intent(text=text)
        decision = self.router.decide(intent)
        status = self.device_service.status(device_id)
        ui_state = UIState(
            view="device_status",
            title="Status do YBY",
            status={"level": "normal", "message": "Dados simulados do dispositivo"},
            components=[
                {"type": "metric", "id": "battery", "label": "Bateria", "value": status.battery_percent, "unit": "%", "source": status.source},
                {"type": "metric", "id": "temperature", "label": "Temperatura", "value": status.temperature_c, "unit": "°C", "source": status.source},
                {"type": "metric", "id": "ble", "label": "BLE", "value": status.ble_connected, "unit": None, "source": status.source},
            ],
        )
        errors = list(self.ui_validator.iter_errors(ui_state.model_dump()))
        if errors:
            raise ValueError(f"generated UI state violates contract: {errors[0].message}")
        return decision.route, decision.reason, ui_state

    def ask_model(self, text: str) -> dict:
        result = self.provider_router.generate(
            ProviderRequest(
                text=text,
                system="Responda em JSON válido. Não invente telemetria nem execute ações.",
                response_schema={"type": "object", "properties": {"answer": {"type": "string"}}, "required": ["answer"]},
            )
        )
        if result.status != "success":
            raise RuntimeError(result.error_code or "provider_error")
        return result.output
