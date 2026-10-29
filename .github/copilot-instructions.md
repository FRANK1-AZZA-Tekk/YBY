# YBY — GitHub Copilot Instructions

Este arquivo configura o GitHub Copilot para entender o projeto YBY e gerar código alinhado com as decisões de arquitetura, princípios e restrições do sistema.

## Identidade do projeto

O YBY (You By Yourself) é um exocórtex pessoal distribuído composto por:

- Um relógio inteligente (LilyGO T-Watch S3 Plus / ESP32-S3)
- Um celular Android (Xiaomi 12 / Termux / sem root)
- Um PC local (Ryzen 5 4600G + GTX 1650)
- Uma camada de nuvem opcional

Princípio fundamental: Function Over Form. Confiabilidade, latência e utilidade vêm antes de qualquer questão estética.

## Regras absolutas — nunca viole estas

- NUNCA sugira rodar um LLM conversacional completo no relógio (ESP32-S3).
- NUNCA assuma que a internet está disponível como requisito para funcionar.
- NUNCA sugira uma solução que não tenha fallback definido.
- NUNCA execute ou sugira comandos ADB destrutivos sem backup e reversão.
- NUNCA envie áudio bruto, dados biométricos ou localização para a nuvem.
- NUNCA gere código que altere o sistema sem possibilidade de rollback.
- NUNCA crie dependência de um único ponto de falha.
- NUNCA ignore o consumo de bateria em código para o relógio ou celular.

## Regras de geração de código

### Geral

- Prefira soluções simples e testáveis a soluções elegantes e complexas.
- Todo código que executa ações críticas deve ter função de reversão documentada.
- Toda feature nova deve incluir comentário com: o que resolve, risco, fallback.
- Priorize baixa latência e baixo consumo sobre completude de features.

### ESP32-S3 (relógio)

- Use NimBLE-Arduino para BLE, não a biblioteca padrão ArduinoBLE (menor footprint).
- Separe tarefas LVGL e BLE em cores diferentes: LVGL no Core 1, BLE no Core 0.
- Coloque código crítico em SRAM interna, assets e buffers em PSRAM.
- Implemente sempre debounce em gestos (mínimo 300 ms entre disparos).
- Desative Wi-Fi no relógio por padrão — toda comunicação vai pelo BLE.
- Use esp_sleep_enable_timer_wakeup() para light-sleep entre eventos.
- Pacotes BLE devem ser JSON compacto com campos curtos (máximo 247 bytes).
- Toda vibração de feedback deve ter duração máxima de 80 ms.

### Android / Termux

- Use Python 3.11+ ou Rust para daemons no Termux.
- Nunca crie mais de 3 processos paralelos sem justificativa de latência.
- Toda comunicação BLE deve ter fila de retry com backoff exponencial.
- SQLite é o banco padrão para memória operacional — sem PostgreSQL, sem MongoDB.
- Modelos de IA locais devem usar llama-cpp-python ou ollama via HTTP local.
- Modelos GGUF quantizados em Q4_K_M como padrão de equilíbrio.
- Nunca carregue modelos maiores que 3 GB na RAM do celular.
- Implemente watchdog para reiniciar serviços que travam.

### PC Hub

- Use llama.cpp com suporte a CUDA (GTX 1650, 4 GB VRAM).
- Modelos de 7–8B quantizados em Q4_K_M são o limite seguro para a VRAM disponível.
- Use LanceDB para banco vetorial local — sem Pinecone, sem Weaviate cloud.
- Exponha API local via FastAPI na porta 11434 (compatível com Ollama).
- Toda API local deve exigir autenticação por token mesmo em rede interna.
- Logs em formato estruturado JSON para facilitar análise posterior.

## IA e modelos

- Tente sempre o modelo local primeiro.
- Só rotear para nuvem quando o modelo local claramente não resolve.
- Antes de qualquer envio para API externa, execute sanitização de dados.
- Sanitização mínima obrigatória: remover nomes próprios, locais, dados financeiros.
- Registre localmente todo uso de API externa com timestamp e tokens consumidos.

## Memória

- Estrutura base em SQLite com tabelas: eventos, tarefas, preferencias, memorias, sessoes, erros, permissoes.
- Embeddings locais com nomic-embed-text ou all-minilm.
- Banco vetorial só entra quando houver mais de 500 memórias registradas.
- Toda memória sensível deve ser criptografada com chave local (AES-256).

## Arquitetura de mensagens BLE

```json
// Evento do relógio para o celular
{"t":"g","g":2,"ts":1724215200,"bat":82}

// Comando do celular para o relógio
{"t":"cmd","cmd":"vibrate","ms":80,"txt":"Tarefa registrada"}

// Status do sistema
{"t":"s","ble":true,"ai":"local","bat":82,"mode":"normal"}
```

Campos curtos são obrigatórios para respeitar o MTU do BLE.

## Roteamento de IA — lógica esperada

```python
def route_task(task, context):
    if context.is_sensitive:
        return "local"
    if local_model.can_handle(task):
        return "local"
    if pc_hub.is_available():
        return "hub"
    if context.allow_cloud:
        sanitize(task)
        return "cloud"
    return "degraded"
```

## Estrutura de pastas esperada

```text
YBY/
├── .github/
│   └── copilot-instructions.md
├── docs/
│   ├── 00-documento-mestre-v1.md
│   ├── 01-firmware-relogio.md
│   ├── 02-celular-termux.md
│   ├── 03-hub-pc.md
│   ├── 04-memoria.md
│   ├── 05-roteador-ia.md
│   ├── 06-seguranca.md
│   └── 07-roadmap.md
├── firmware/
│   └── twatch-s3-plus/
├── mobile/
│   └── termux/
├── hub/
│   └── pc/
├── memory/
│   └── schemas/
└── tests/
    └── benchmarks/
```

## Padrão de comentários para decisões

```python
# [YBY-DECISION] motivo da escolha
# Alternativa considerada: X
# Por que não: Y
# Fallback: Z
```

```cpp
// [YBY-DECISION] motivo da escolha
// Alternativa considerada: X
// Por que não: Y
// Fallback: Z
```

## Checklist antes de sugerir qualquer código

- Funciona offline?
- Tem fallback se falhar?
- Consome bateria de forma aceitável?
- Tem possibilidade de rollback?
- Não envia dados sensíveis sem sanitização?
- Respeita os limites de memória do dispositivo alvo?
- Tem log da ação?
- Tem teste mínimo associado?

## O que o YBY nunca deve fazer

- Nunca gravar áudio em background sem VAD confirmando presença de voz
- Nunca enviar localização para serviços externos
- Nunca executar código gerado sem sandbox e confirmação do usuário
- Nunca apagar memórias sem aprovação explícita
- Nunca instalar atualizações sem relatório prévio e possibilidade de rollback
- Nunca depender de um único provedor de IA
- Nunca expor a API local sem autenticação, mesmo em rede doméstica
