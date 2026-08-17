# YBY
Repository name:YBY [You By Yourself]® — Wearable opensource com IA   

<div align="center">

# YBY — You By Yourself®

**Wearable opensource com IA de alto impacto social**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Hardware](https://img.shields.io/badge/Hardware-LilyGO_T--Watch_S3_Plus-blue)](docs/YBY-HW-IDENTITY-001.md)
[![LVGL](https://img.shields.io/badge/LVGL-9.4.0-green)](https://lvgl.io)
[![Arduino Core](https://img.shields.io/badge/Arduino_Core-3.3.4-orange)](https://github.com/espressif/arduino-esp32)

</div>

---

## O que é o YBY

YBY é um projeto opensource focado em educação e tecnologia de alto impacto social.
O objetivo é criar um wearable inteligente, acessível e extensível que funciona como
assistente pessoal local-first — sem depender de nuvem para funcionar.

**Lema:** Function over Form.

---

## Hardware

| Componente | Detalhe |
|---|---|
| Placa | LilyGO T-Watch S3 Plus (Add GPS) |
| MCU | ESP32-S3 — 16MB Flash, 8MB PSRAM |
| Display | ST7789V, 1.54", 240×240, SPI |
| Touch | FT6336U capacitivo |
| GPS | u-blox MIA-M10Q |
| LoRa | Semtech SX1262 |
| PMU | X-Powers AXP2101 |
| IMU | Bosch BMA423 |
| Haptics | TI DRV2605 |
| Áudio | MAX98357A + PDM SPM1423HM4H-B |
| RTC | NXP PCF8563 |
| Bateria | 940 mAh |

---

## Arquitetura

```
yby_platform     → drivers de hardware (PMU, display, touch, RTC, IMU, GPS)
yby_domain       → lógica de domínio (intents, contexto, estados)
yby_runtime      → supervisor, watchdog, event bus, telemetria
yby_ui           → interface LVGL, avatar, navegação
yby_gateway      → protocolo BLE, fila offline, sync
```

---

## Documentos técnicos

| Documento | Descrição |
|---|---|
| [YBY-PROTO-001](docs/YBY-PROTO-001.md) | Protocolo BLE completo |
| [YBY-HW-IDENTITY-001](docs/YBY-HW-IDENTITY-001.md) | Identidade do hardware |
| [YBY-GPIO-MAP-001](docs/YBY-GPIO-MAP-001.md) | Mapa de GPIO validado |
| [YBY-PMIC-MAP-001](docs/YBY-PMIC-MAP-001.md) | Canais do AXP2101 |

---

## Roadmap

- [x] Identidade de hardware confirmada
- [x] Protocolo BLE definido (YBY-PROTO-001)
- [ ] Sprint 0 — Ambiente e backup do firmware
- [ ] Sprint 1 — Hardware baseline
- [ ] Sprint 2 — UI e energia
- [ ] Sprint 3 — BLE e gateway Android
- [ ] Sprint 4 — Contexto e offline
- [ ] Sprint 5 — Telemetria
- [ ] Sprint 6 — Migração ESP-IDF

---

## Contribuindo

Este projeto é opensource e educacional. Toda contribuição é bem-vinda.
Leia os documentos em `/docs` antes de abrir um PR.

---

## Licença

MIT — veja [LICENSE](LICENSE)

---

<div align="center">
LINKK TEKK · Jundiaí, Brasil · 2026
</div> 