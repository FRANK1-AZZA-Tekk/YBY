# YBY AI System v2

## Visão

O YBY é um ecossistema open source de IA pessoal vestível, híbrida e centrada no ser humano.

Princípio: **Function over Form**.

## Arquitetura

- Interface: Open WebUI, app/dashboard e wearable
- Orquestração: LangGraph
- Modelos locais: Ollama
- Memória: Mem0 + SQLite/Postgres
- RAG: Nomic Embed Text + Qdrant ou pgvector
- Ferramentas: MCP
- Pesquisa externa: Perplexity Sonar e OpenRouter
- Backend: FastAPI
- Wearable: LilyGO T-Watch S3 Plus, ESP-IDF, FreeRTOS e LVGL

## Enxame de agentes

1. **YBY Orchestrator** — classifica intenção, coordena agentes e sintetiza respostas.
2. **Archivist** — memória de longo prazo, notas, projetos e recuperação semântica.
3. **Technician** — hardware, firmware, energia, sensores e compatibilidade.
4. **Researcher** — pesquisa externa, comparações e fontes atualizadas.
5. **Builder** — código, scripts, testes e firmware.
6. **Operator** — Calendar, Gmail, arquivos e automações.
7. **Guardian** — políticas de segurança, permissões e auditoria.

## Roteamento

| Ação | Agente primário | Ferramentas |
|---|---|---|
| Comando simples | Núcleo determinístico | Nenhuma |
| Pergunta pessoal | Archivist + Qwen | RAG |
| Hardware | Technician | RAG, busca externa |
| Pesquisa | Researcher | Perplexity/OpenRouter |
| Código | Builder | Qwen-Coder, Git |
| Imagem | Visão local | Qwen2.5-VL 3B |
| Ação externa | Operator + Guardian | MCP, aprovação humana |
| Voz | Whisper + Piper | STT e TTS locais |

## Modelos recomendados

- Qwen2.5 3B Instruct Q4: assistente principal
- Llama 3.2 3B: roteador e comandos
- Nomic Embed Text: embeddings/RAG
- Qwen2.5-VL 3B: visão, opcional
- Qwen2.5-Coder 3B: programação, opcional
- Whisper base/small: transcrição
- Piper pt-BR: síntese de voz

## Configuração do Ollama

```bash
OLLAMA_KEEP_ALIVE=10m
OLLAMA_MAX_LOADED_MODELS=1
OLLAMA_NUM_PARALLEL=1
OLLAMA_CONTEXT_LENGTH=4096
```

## Segurança

- Menor privilégio para todas as credenciais
- Separação entre ferramentas de leitura e escrita
- Aprovação humana obrigatória para ações externas, financeiras ou irreversíveis
- Proibição de indexar segredos, tokens, senhas e dados biométricos brutos
- Logs de auditoria para cada tool call
- Acesso remoto apenas por Tailscale ou VPN

## RAG

- Formato preferencial: Markdown
- Chunk: 1.000 tokens
- Overlap: 200 tokens
- Top-K: 3 a 5
- Splitting por cabeçalhos Markdown
- Metadados: título, data, projeto, tags, status e fonte

## Roadmap

1. Hub local com Ollama, Open WebUI, RAG e FastAPI
2. Memória persistente e MCP de arquivos/Calendar
3. Agentes LangGraph com aprovação humana
4. Integração Xiaomi via Termux e Tailscale
5. Firmware YBY Zero no LilyGO T-Watch S3 Plus
6. Night Watch, voz, visão e automações

## Princípio de operação

O wearable coleta contexto e entrega feedback.
O PC processa, decide e guarda memória.
O celular atua como gateway e camada de fallback.
A nuvem é acionada somente quando agrega pesquisa, capacidade ou fontes reais.
