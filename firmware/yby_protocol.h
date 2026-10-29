/* YBY-PROTO-001 v1.0 - Protocolo de Comunicação BLE
 * Status: OFICIAL - CONGELADO APÓS SPRINT 3
 * Hardware: LilyGO T-Watch S3 Plus (YBY-WATCH-001)
 *
 * YBY_SERVICE_UUID = 3f033f83-6423-4390-87b1-33773a6e6f8d
 * Nome BLE: YBY-WATCH
 * Intervalo: 100ms durante advertising ativo; 500ms após 60s sem conexão.
 *
 * Frame (máx. 216 bytes):
 * 0     version (uint8) = 1
 * 1     type (uint8) - yby_frame_type_t
 * 2-3   id (uint16)
 * 4-5   sequence (uint16)
 * 6     priority (uint8)
 * 7-8   ttl_ms (uint16)
 * 9-10  length (uint16)
 * 11-14 auth[4] - HMAC-SHA256 truncado
 * 15    reservado
 * 16-215 payload[200]
 *
 * Tipos: 0x00 CMD, 0x01 EVENT, 0x02 TELEMETRY, 0x03 ACK, 0x04 SYNC, 0xFF ERROR
 * Prioridades: P0 crítico (nunca descarta), P1 importante (fila 50), P2 informativo (fila 100)
 *
 * Estados de energia:
 * ACTIVE >= 3800 mV; AMBIENT 3600-3799; SAVE 3400-3599; CRITICAL 3200-3399; SHUTDOWN < 3200.
 *
 * Estados: IDLE, LISTENING, THINKING, SPEAKING, ERROR, OFFLINE, LOW_POWER, PRIVACY.
 * BLE: ADVERTISING, CONNECTING, CONNECTED, DISCONNECTED, OFF.
 *
 * auth = HMAC-SHA256(key=YBY_SHARED_KEY, data=payload)[0:4]
 *
 * Nota de auditoria: HMAC truncado em 4 bytes é curto para autenticação;
 * revisar antes do congelamento no Sprint 3.
 */

#ifndef YBY_PROTOCOL_H
#define YBY_PROTOCOL_H

#include <stdint.h>

#define YBY_PROTOCOL_VERSION 1
#define YBY_MTU_TARGET 247
#define YBY_FRAME_MAX 216
#define YBY_PAYLOAD_MAX 200

#define YBY_SERVICE_UUID "3f033f83-6423-4390-87b1-33773a6e6f8d"
#define YBY_DEVICE_NAME "YBY-WATCH"
#define YBY_HARDWARE_ID "YBY-WATCH-001"

typedef enum {
    YBY_FRAME_CMD = 0x00,
    YBY_FRAME_EVENT = 0x01,
    YBY_FRAME_TELEMETRY = 0x02,
    YBY_FRAME_ACK = 0x03,
    YBY_FRAME_SYNC = 0x04,
    YBY_FRAME_ERROR = 0xFF
} yby_frame_type_t;

typedef enum {
    YBY_PRIORITY_P0 = 0x00,
    YBY_PRIORITY_P1 = 0x01,
    YBY_PRIORITY_P2 = 0x02
} yby_priority_t;

typedef enum {
    YBY_INTENT_NONE = 0x0000,
    YBY_INTENT_PING = 0x0001,
    YBY_INTENT_GET_STATUS = 0x0002,
    YBY_INTENT_GET_IDENTITY = 0x0003,
    YBY_INTENT_SET_CONTEXT = 0x0010,
    YBY_INTENT_CLEAR_CONTEXT = 0x0011,
    YBY_INTENT_GET_CONTEXT = 0x0012,
    YBY_INTENT_HAPTIC_PULSE = 0x0020,
    YBY_INTENT_DISPLAY_MSG = 0x0021,
    YBY_INTENT_CLEAR_MSG = 0x0022,
    YBY_INTENT_SET_BRIGHTNESS = 0x0023,
    YBY_INTENT_SYNC_TIME = 0x0030,
    YBY_INTENT_SET_ALARM = 0x0031,
    YBY_INTENT_CANCEL_ALARM = 0x0032,
    YBY_INTENT_EXPORT_LOG = 0x0040,
    YBY_INTENT_CLEAR_LOG = 0x0041,
    YBY_INTENT_EXPORT_IDENTITY = 0x0042,
    YBY_INTENT_SAFE_MODE = 0x00F0,
    YBY_INTENT_RESTART = 0x00F1,
    YBY_INTENT_FACTORY_RESET = 0x00FE,
    YBY_INTENT_SHUTDOWN = 0x00FF
} yby_intent_t;

typedef enum {
    YBY_MODE_IDLE = 0x00,
    YBY_MODE_LISTENING = 0x01,
    YBY_MODE_THINKING = 0x02,
    YBY_MODE_SPEAKING = 0x03,
    YBY_MODE_ERROR = 0x04,
    YBY_MODE_OFFLINE = 0x05,
    YBY_MODE_LOW_POWER = 0x06,
    YBY_MODE_PRIVACY = 0x07
} yby_mode_t;

typedef struct {
    uint8_t version;
    uint8_t type;
    uint16_t id;
    uint16_t sequence;
    uint8_t priority;
    uint16_t ttl_ms;
    uint16_t length;
    uint8_t auth[4];
    uint8_t reserved;
    uint8_t payload[YBY_PAYLOAD_MAX];
} yby_frame_t;

#endif /* YBY_PROTOCOL_H */
