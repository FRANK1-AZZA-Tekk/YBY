# API local do YBY

## Objetivo

A API local é a primeira vertical slice executável do YBY. Nesta etapa ela usa apenas dados simulados e roteamento local. Não acessa OpenRouter, Ollama, BLE ou hardware real.

## Executar

Instale as dependências de desenvolvimento:

```bash
python -m pip install ".[dev]"
```

Inicie o servidor:

```bash
uvicorn yby.api.app:app --reload --host 127.0.0.1 --port 8787
```

Documentação interativa:

```text
http://127.0.0.1:8787/docs
```

## Endpoints

### `GET /health`

Retorna o estado da API.

### `GET /api/device/status`

Retorna telemetria simulada do dispositivo. A resposta contém `source: simulated` para evitar confundir dados de demonstração com medições reais.

### `POST /api/intent`

Exemplo:

```json
{"text":"Como está o YBY?","device_id":"yby-dev-001"}
```

Retorna a rota escolhida e um estado de UI validável pelo contrato `ui_state.schema.json`.

## Limitações atuais

- Sem autenticação.
- Sem OpenRouter.
- Sem Ollama.
- Sem BLE.
- Sem hardware real.
- Sem persistência.

Esta API deve ser usada somente em `127.0.0.1` durante o MVP.
