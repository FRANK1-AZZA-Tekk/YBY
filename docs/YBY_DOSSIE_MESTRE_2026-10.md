# YBY — Dossiê Mestre Compilado (out/2026)

## Resumo executivo
YBY (You By Yourself) é um ecossistema open source de wearables e IA híbrida local/nuvem, um "exocórtex" pessoal distribuído. Princípio central: **o PC pensa, o Xiaomi intermedia, os ESP32 percebem e atuam**, com fallback em cascata. Lema: **Function over Form**.

## Arquitetura em camadas
- **PC (cérebro principal):** NOMAD, Ollama, LiteLLM/OpenRouter, RAG, memória, orquestração de agentes.
- **Xiaomi 12 (secundário/gateway):** conecta ao PC via Tailscale; modelo leve (~3B) quando necessário.
- **Wearables/ESP32 (percepção/ação):** LilyGO T-Watch S3 Plus, XIAO ESP32-S3 Sense, Guition ESP32-P4+C6, AtomS3R; regras determinísticas e IA mínima offline.
- **Fallback:** PC -> Xiaomi -> T-Watch/regras locais -> modo degradado seguro.

## YBY SEED (MVP)
- Foco no PC antes de expandir para wearables.
- Stack: Ollama (local), OpenRouter (nuvem), LiteLLM (roteamento/custo), Cursor Pro (implementação), Perplexity/Gemini (pesquisa/revisão).
- Fluxo: entrevista por voz -> requisitos -> debate local -> revisão em nuvem -> implementação -> autorização do usuário.

## Roteamento de IA (local-first)
- Local (Ollama) quando qualidade/latência permitem; nuvem quando há ganho real.
- Dados sensíveis permanecem offline; limites de orçamento por chave/API.

## Memória e agentes
- Event log estruturado (JSON); memória curta (KV cache); memória longa (banco vetorial + SQLite/Supabase) com compressão periódica.
- Multi-agente: orquestrador + especialistas (voz, automação, visão, planejamento, segurança) + dev assistido.

## Hardware
- PC: Ryzen 5 4600G, 16 GB RAM, GTX 1650 4 GB, SSD 1 TB.
- Xiaomi 12 (8 GB RAM), T-Watch S3 Plus, Guition ESP32-P4+C6, XIAO ESP32-S3 Sense, AtomS3R + Echo Base, Radxa ROCK 4D, power bank 20.000 mAh, painel solar 30 W (futuro).

## Energia, comunicação e segurança
- Deep sleep agressivo, DFS, medição de Wh/dia por nó.
- MQTT/MQTTS, BLE, ESP-NOW/LoRa, Tailscale.
- Sandbox, permissões por nível, TLS, logs de auditoria; local por padrão.

## Tendências (semana de 20-27/out/2026)
- **MemT-1.0** (memória nativa; ~66x menos storage a 128K tokens; código PolyForm Noncommercial, paper CC-BY-NC-SA — atenção à licença): inspiração para a camada de memória do YBY, sem copiar código.
- **DeepInfer** (DeepSeek, Apache 2.0): filosofia de cache, quantização e agendamento determinístico.
- **Multi-agente e AI-native dev** (Gartner 2026): blueprint da arquitetura de agentes.
- **Physical AI e world models** (WEF/Juniper 2026): roadmap futuro.
- **OpenArm 2.0 / OpenAMRobot**: referência open source de robótica (CERN-OHL-S / Apache-2.0).

## Roadmap
1. YBY SEED PC v0.1 (Docker, Ollama, LiteLLM, RAG, memória, API).
2. Voz (faster-whisper) em PT-BR.
3. Xiaomi como gateway (Tailscale + modelo 3B).
4. T-Watch S3 Plus como nó mínimo.
5. Cyberdeck Guition + mouse-anel BLE + LVGL.
6. Visão POV, TinyML e physical AI.

## Próximos passos
- Contrato de API do cérebro (OpenAPI).
- Device Registry v0.1 (SQLite, descoberta, permissões).
- Pipeline RAG + memória (embedding, chunking, banco vetorial).
- Documentação em PT-BR para a comunidade.
