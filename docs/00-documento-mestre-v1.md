# YBY — Documento Mestre v1.0

You By Yourself | Exocórtex Pessoal Distribuído  
Princípio: Function Over Form  
Data: 2026-08-21

## 1. Visão

O YBY é um exocórtex pessoal distribuído: um sistema que percebe contexto, registra memória útil, executa tarefas de baixo risco, aprende com o usuário e continua funcionando mesmo quando partes da infraestrutura falham.

Princípios do projeto:

- Local-first: o sistema deve funcionar offline sempre que possível.
- Function Over Form: confiabilidade, latência e utilidade vêm antes da estética.
- Modularidade: relógio, celular, PC e nuvem funcionam em camadas independentes.
- Segurança por padrão: sanitização, confirmação para ações críticas e rollback.
- Evolução supervisionada: o sistema sugere melhorias, mas não se altera cegamente.

## 2. Arquitetura geral

[T-Watch S3 Plus] <-> BLE <-> [Xiaomi 12 / Termux] <-> Wi-Fi/Tailscale <-> [PC YBY Hub] <-> [Nuvem opcional]

- YBY Wear: relógio como sensor, atuador e fallback de emergência.
- YBY Pocket: celular como orquestrador principal do MVP.
- YBY Hub: PC como hub local para inferência mais pesada, memória longa e automações.
- YBY Cloud: camada opcional para tarefas complexas, nunca requisito do core.

## 3. Hardware confirmado

- Wearable: LilyGO T-Watch S3 Plus (ESP32-S3).
- Mobile: Xiaomi 12, Android 15 / HyperOS 3.0, Termux.
- Hub local: PC Ryzen 5 4600G, GTX 1650 4 GB, 16 GB RAM.
- Futuro: ESP32-P4 + ESP32-C6 com tela 4.3", AtomS3R-CAM e outros módulos multimodais como extensões.

## 4. Decisões fechadas

- Nome do assistente: YBY.
- Público atual: uso pessoal com visão futura open source.
- Idioma interno: inglês quando houver ganho real; interface e entendimento em português do Brasil.
- PC pode ser usado como cérebro pesado e fica ligado 24h.
- Rede principal: Wi-Fi local + Tailscale.
- Terminal ESP32-P4/C6 não entra no MVP.
- Resposta preferida: voz + texto adaptados ao contexto.
- Backup: local + nuvem criptografada.
- Relatório de melhoria: diário, com opção de rollback.

## 5. Relógio (YBY Wear)

O relógio não é o cérebro principal. Ele sente, sinaliza, ativa o sistema e mantém um fallback mínimo quando o celular falha.

Ativação híbrida: toque como padrão, microgestos como atalho, voz como alternativa contextual.

Sete microgestos base: levantar o pulso, girar para dentro, girar para fora, toque duplo, toque triplo, sacudir suavemente, segurar o pulso parado.

Cada gesto deve ter: limiar configurável, anti-repetição, feedback háptico, log de falso positivo, possibilidade de desativação.

Tela glanceable: linha de status fixa, item principal de foco, última resposta curta, três ações rápidas.

IA de emergência: comandos básicos fixos (timer, alarme, nota rápida, última tarefa), consulta local a arquivos essenciais, armazenamento temporário de eventos para sincronizar depois.

## 6. Celular (YBY Pocket)

O Xiaomi 12 é o orquestrador principal do MVP.

Responsabilidades: receber eventos do relógio via BLE, transformar voz em texto, classificar intenção, executar tarefas de baixo risco, rotear para IA local/PC/nuvem, manter memória operacional, continuar funcionando sem o PC.

IA local no celular: meta de resposta aceitável em até ~5 segundos.

Tarefas de baixo risco sem confirmação constante: criar nota, registrar evento simples, timer, alarme, memória operacional, status interno.

## 7. PC (YBY Hub)

Responsabilidades: inferência local mais forte, memória de longo prazo, RAG local, automações, processamento demorado, backup e observabilidade.

Motor preferido: llama.cpp com modelos GGUF quantizados.

## 8. Nuvem opcional

Regra: tentar local primeiro; antes de enviar dados, sanitizar nomes, locais e informações sensíveis.

## 9. Memória

Estratégia: contexto automático + captura de memórias amplas, com curadoria humana.

Revisão a cada 3 dias com cartões de memória: memória curta, memória longa, importante, sensível, descartar.

## 10. Personalidade e adaptação

O YBY aprende continuamente com o usuário e adapta tom, vocabulário, grau de detalhe, idioma misto e contexto de uso.

## 11. Roteador de áudio

O relógio entende o contexto e escolhe a melhor opção de captura com menor latência e melhor qualidade; quando útil, prefere fone; VAD local é o padrão desejado.

## 12. Notificações proativas

O YBY pode avisar proativamente qualquer coisa relevante, respeitando contexto, prioridade e ruído cognitivo.

## 13. Autoprogramação

Comandos simples podem executar direto; mudanças estruturais precisam de confirmação; tudo deve rodar com possibilidade de reversão.

## 14. Rotina de manutenção

Janela automática diária com relatório posterior: relatório matinal, rollback de versão, checagem de integridade, limpeza de estado ruim, reinício de serviços.

Rollback automático é permitido se uma atualização quebrar o sistema.

## 15. Segurança

Local-first, zero trust entre módulos, confirmação para ações críticas, sanitização antes da nuvem, logs e auditoria, rollback disponível, isolamento para código gerado.

## 16. Pós-MVP

Integrações desejadas: Google Calendar, Google Tasks, WhatsApp, e-mail, Spotify e outras integrações úteis.

## 17. Roadmap resumido

- Fase 1: firmware do relógio, BLE estável, microgestos, feedback háptico, comandos básicos.
- Fase 2: IA local no celular, STT local, memória operacional, roteamento básico.
- Fase 3: hub PC com llama.cpp, RAG local, sincronização celular-PC.
- Fase 4: cartões de memória, personalidade adaptativa, relatórios de melhoria.
- Fase 5: integrações externas, terminal opcional, multimodalidade expandida.

## 18. Estrutura sugerida do repositório

YBY/ com docs/, firmware/twatch-s3-plus/, mobile/termux/, hub/pc/, memory/schemas/, tests/.

## 19. Regras para o Cursor e para a equipe

Preferir soluções simples e testáveis; nunca assumir cloud como dependência; nunca colocar LLM completo no relógio; otimizar para latência, confiabilidade e rollback; toda feature nova deve dizer o que resolve, custo, risco, consumo e fallback; toda automação deve ter possibilidade de desfazer; toda mudança crítica deve ser registrada em changelog.

## 20. Próximo arquivo recomendado

docs/01-firmware-relogio.md — detalhar hardware do T-Watch S3 Plus, BLE, microgestos, VAD, UI glanceable e fallback de emergência.
