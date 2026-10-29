# YBY-HW-IDENTITY-001 — Identidade do Hardware

**Status:** CONFIRMED_BY_DEVICE  
**Data:** 2026-08-06  
**Fonte:** leitura direta do painel de diagnóstico do firmware de fábrica

## Unidade

| Campo | Valor |
|---|---|
| ID | YBY-WATCH-001 |
| Produto | LilyGO T-Watch S3 Plus |
| Variante | Add GPS |
| Chip ID | EC353313CFD0 |
| MAC | D0:CF:13:33:35:EC |
| Build date | Dec 19 2025 16:14:14 |

## Hardware confirmado

| Componente | Detalhe | Status |
|---|---|---|
| MCU | ESP32-S3 | OK |
| Flash | 16 MB QSPI | OK |
| PSRAM | 8 MB QSPI | OK |
| Display | ST7789V, 1.54", 240x240, SPI | OK |
| Touch | FT6336U capacitivo | OK |
| GPS | u-blox MIA-M10Q | OK |
| LoRa | Semtech SX1262 | OK |
| PMU | X-Powers AXP2101 | OK |
| IMU | Bosch BMA423 | OK |
| Haptics | TI DRV2605 | OK |
| Áudio out | MAX98357A I2S Class D | OK |
| Microfone | PDM SPM1423HM4H-B | OK |
| RTC | NXP PCF8563 | OK |
| IR | GPIO 2 | OK |
| Bateria | 940 mAh | OK |
| Storage disponível | 7.00 MB | OK |

## Firmware de referência

| Item | Valor |
|---|---|
| LVGL | 9.4.0 |
| Arduino Core | 3.3.4 |

## Módulos online (painel de diagnóstico)

SX1262, Touch, DRV2605, AXP2101, PCF8563, PSRAM, MIA-M10Q, BMA423 — todos OK.

## Leituras dinâmicas

| Leitura | Valor | Observação |
|---|---|---|
| Tensão da bateria | 4143-4148 mV | próxima de cheia |
| Data/hora RTC | 2026/08/06 13:53:24 | RTC funcional |

## Notas

- Fuel gauge do AXP2101 não calibrado — usar tensão bruta
- Touch reset não conectado — nunca colocar FT6336U em sleep
- Corrente de carga máxima: 400 mA
