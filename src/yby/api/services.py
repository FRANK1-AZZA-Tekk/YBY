"""Application services for the first local YBY API."""

from yby.core.models import Intent
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
        self.device_service = DeviceService()

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
        return decision.route, decision.reason, ui_state
