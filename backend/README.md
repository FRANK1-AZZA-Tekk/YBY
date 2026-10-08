# YBY Hub — Backend FastAPI

Estrutura inicial do hub local do ecossistema YBY.

## Executar localmente

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## Endpoints

- `GET /` — informações do hub
- `GET /health` — verificação de saúde
- `POST /ai/chat` — interação com o modelo local via Ollama
- `GET /docs` — documentação interativa

## Princípio

O backend mantém o roteamento simples: um modelo padrão carregado,
com especialistas acionados apenas quando a tarefa exigir.
Ações externas ou irreversíveis exigem aprovação humana.
