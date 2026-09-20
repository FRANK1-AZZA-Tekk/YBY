# YBY ZERO

YBY ZERO é o núcleo inicial do ecossistema YBY: uma plataforma wearable conversacional, distribuída e offline-first.

## Arquitetura

- **PC:** cérebro principal, memória, RAG e inferência local.
- **Xiaomi 12:** gateway de áudio, roteamento e fallback móvel.
- **Fones:** entrada e saída de voz.
- **T-Watch S3 Plus:** status, vibração, confirmação e modo seguro.
- **Ollama:** inferência local.
- **OpenRouter:** roteamento externo e fallback opcional.
- **Gemini Live/OpenAI Realtime:** camada premium de voz em tempo real.

## Pilares v0.1

1. Eventos versionados.
2. Roteamento por privacidade, latência, custo e capacidade.
3. Voz em tempo real com providers substituíveis.
4. Privacidade por níveis P0–P3.
5. Observabilidade por interação.
6. Degradação segura e fallback progressivo.

## Princípios

- Function over Form.
- Offline-first.
- Privacidade por padrão.
- Fallback progressivo.
- Provedores substituíveis.
- Eventos versionados.

## Desenvolvimento

```bash
python -m venv .venv
source .venv/bin/activate
make install
make test
```

Nenhuma chave de API deve ser commitada. Use `.env` local a partir de `.env.example`.
