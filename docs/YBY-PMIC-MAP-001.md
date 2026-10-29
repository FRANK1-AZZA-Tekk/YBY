# YBY-PMIC-MAP-001 — Canais do AXP2101

**Status:** CONFIRMED_BY_OFFICIAL_DOCS  
**Fonte:** LilyGoLib docs (lilygo-t-watch-s3-plus.md)

## Mapa de canais

| Canal | Periférico | Observação |
|---|---|---|
| DC1 | ESP32-S3 | NUNCA desligar |
| DC2 | Não usado | — |
| DC3 | Não usado (era GPS versão antiga) | não usar para GPS |
| DC4 | Versão LS550G apenas | — |
| DC5 | Não usado | — |
| LDO1 (VRTC) | Não usado | — |
| ALDO1 | Não usado | — |
| ALDO2 | Display Backlight | — |
| ALDO3 | Display + Touch | desligar juntos |
| ALDO4 | LoRa SX1262 | desligar quando LoRa não usado |
| BLDO1 | GPS MIA-M10Q | ativar antes de usar GPS |
| BLDO2 | DRV2605 enable | ativar antes de vibrar |
| DLDO1 | Não usado | — |
| CPUSLDO | Não usado | — |
| VBACKUP | RTC Button Battery | mantém PCF8563 com energia |

## Parâmetros elétricos

| Parâmetro | Valor |
|---|---|
| Entrada USB | 3.9V - 6V |
| Corrente de carga | 0 - 1024 mA (programável) |
| Corrente máxima recomendada | 300 - 400 mA |
| Tensão nominal da bateria | 3.7V |
| Capacidade da bateria | 940 mAh |

## Consumo por modo (medido pelo fabricante)

| Modo | Wake por | Corrente |
|---|---|---|
| Light-Sleep | Touch + botões | 2.38 mA |
| Deep-Sleep | Touch | 1.08 mA |
| Deep-Sleep | Timer (backup on) | 510 uA |
| Deep-Sleep | Timer (backup off) | 460 uA |
| Deep-Sleep | Botões (backup on) | 530 uA |
| Power OFF | Só backup ativo | 50 uA |

## Regras de operação

1. DC1 nunca desliga — é o canal do ESP32-S3
2. ALDO3 desliga display e touch juntos — nunca separar
3. BLDO1 para GPS — versão Plus com botão traseiro usa BLDO1, não DC3
4. Corrente de carga <= 400 mA — risco de dano físico acima disso
5. Fuel gauge não calibrado — usar tensão bruta (battery_mv), não percentual
