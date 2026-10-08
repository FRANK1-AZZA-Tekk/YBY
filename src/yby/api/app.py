"""FastAPI application for the local YBY MVP."""

from fastapi import FastAPI

from .models import DeviceStatus, HealthResponse, IntentRequest, IntentResponse
from .services import DeviceService, IntentService

app = FastAPI(title="YBY Local API", version="0.1.0")
device_service = DeviceService()
intent_service = IntentService()


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@app.get("/api/device/status", response_model=DeviceStatus)
def device_status(device_id: str = "yby-dev-001") -> DeviceStatus:
    return device_service.status(device_id)


@app.post("/api/intent", response_model=IntentResponse)
def process_intent(request: IntentRequest) -> IntentResponse:
    route, reason, ui_state = intent_service.process(request.text, request.device_id)
    return IntentResponse(route=route, reason=reason, ui_state=ui_state)
