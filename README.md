# YBY — You By Yourself®

Wearable open source com IA de alto impacto social.

O YBY usa um LilyGO T-Watch S3 Plus como plataforma experimental para
educação, acessibilidade, autonomia tecnológica e interação local-first.

> Function over form.

## Hardware

- LilyGO T-Watch S3 Plus
- ESP32-S3
- Display 240×240
- Touch capacitivo
- GPS MIA-M10Q
- LoRa SX1262
- AXP2101
- BMA423
- DRV2605
- PCF8563
- MAX98357A
- Microfone PDM

## Documentação

- [Identidade do hardware](docs/YBY-HW-IDENTITY-001.md)
- [Mapa de GPIO](docs/YBY-GPIO-MAP-001.md)
- [Mapa do PMIC](docs/YBY-PMIC-MAP-001.md)
- [Protocolo BLE](docs/YBY-PROTO-001.md)

## Roadmap

- [x] Identidade do hardware
- [x] Mapa de GPIO
- [x] Mapa do PMIC
- [x] Cabeçalho inicial do protocolo
- [x] Constantes Kotlin do protocolo
- [ ] Validar ambiente Arduino
- [ ] Validar display e touch
- [ ] Validar PMIC, RTC e IMU
- [ ] Implementar interface inicial
- [ ] Implementar BLE
- [ ] Criar gateway Android
- [ ] Migrar para ESP-IDF

## Licença MIT.