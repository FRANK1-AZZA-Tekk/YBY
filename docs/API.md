# API local do YBY

## Objetivo

A API local é a primeira vertical slice executável do YBY. Nesta etapa ela usa dados simulados e roteamento local. Não acessa OpenRouter, Ollama, BLE ou hardware real.

## Executar

```bash
python -m pip install ".[dev]"
uvicorn yby.api.app:app --reload --host 127.0.0.1 --port 8787
```

Documentação interativa: `http://127.0.0.1:8787/docs`

## Endpoints

- `GET /health`: disponibilidade da API.
- `GET /version`: versão da API e dos contratos.
- `GET /api/device/status`: telemetria simulada.
- `POST /api/intent`: intenção → rota local → UIState validado.

A API rejeita campos desconhecidos nos modelos de entrada e verifica a resposta de UI contra `contracts/ui_state.schema.json` antes de retorná-la.

## Limitações atuais

- Sem autenticação.
- Sem OpenRouter.
- Sem Ollama.
- Sem BLE.
- Sem hardware real.
- Sem persistência.

Use somente em `127.0.0.1` durante o MVP.
