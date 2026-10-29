# YBY-GPIO-MAP-001 — Mapa de GPIO

**Status:** CONFIRMED_BY_OFFICIAL_DOCS  
**Fonte:** LilyGoLib docs (lilygo-t-watch-s3-plus.md)

## GPIO Map

| Componente | Função | GPIO |
|---|---|---|
| I2C0 | SDA | 10 |
| I2C0 | SCL | 11 |
| FT6336U Touch | SDA | 39 |
| FT6336U Touch | SCL | 40 |
| FT6336U Touch | INT | 16 |
| PCF8563 RTC | INT | 17 |
| BMA423 IMU | INT | 14 |
| AXP2101 PMU | INT | 21 |
| SX1262 LoRa | SCK | 3 |
| SX1262 LoRa | MISO | 4 |
| SX1262 LoRa | MOSI | 1 |
| SX1262 LoRa | RESET | 8 |
| SX1262 LoRa | BUSY | 7 |
| SX1262 LoRa | CS | 5 |
| SX1262 LoRa | INT | 9 |
| Display ST7789V | CS | 12 |
| Display ST7789V | MOSI | 13 |
| Display ST7789V | SCK | 18 |
| Display ST7789V | DC | 38 |
| Display ST7789V | Backlight | 45 |
| GPS MIA-M10Q | TX | 42 |
| GPS MIA-M10Q | RX | 41 |
| MAX98357A Áudio | BCLK | 48 |
| MAX98357A Áudio | WCLK | 15 |
| MAX98357A Áudio | DOUT | 46 |
| PDM Mic | SCK | 44 |
| PDM Mic | DATA | 47 |
| IR TX | — | 2 |

## I2C Addresses

| Dispositivo | Endereço | Barramento |
|---|---|---|
| FT6336U Touch | 0x38 | Wire1 (exclusivo) |
| BMA423 | 0x19 | Wire0 compartilhado |
| AXP2101 | 0x34 | Wire0 compartilhado |
| PCF8563 | 0x51 | Wire0 compartilhado |
| DRV2605 | 0x5A | Wire0 compartilhado |

## Notas críticas

- Touch usa Wire1 exclusivo — não misturar com Wire0
- Display RESET e MISO não conectados
- GPS PPS não conectado
- Touch RESET não conectado — nunca colocar FT6336U em sleep
