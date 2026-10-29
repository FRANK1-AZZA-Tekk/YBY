/**
 * YBY-PROTO-001 v1.0 — Constantes do protocolo BLE para Android
 * Equivalente Kotlin de firmware/yby_protocol.h
 * Manter sempre sincronizado com o firmware.
 */
package yby.gateway

import java.util.UUID

object YbyProtocol {

    // UUIDs BLE (imutáveis após Sprint 3)
    val SERVICE_UUID    = UUID.fromString("3f033f83-6423-4390-87b1-33773a6e6f8d")
    val CHAR_BATTERY    = UUID.fromString("5849b39a-563a-4d40-9310-f1ba1de607f3")
    val CHAR_RTC        = UUID.fromString("fc02a2f8-1502-4209-b31a-acf5eccc4697")
    val CHAR_CMD_IN     = UUID.fromString("61d0290f-7b92-43a5-a7ab-865a2c8e1491")
    val CHAR_EVENT_OUT  = UUID.fromString("b4e7f1a2-9c3d-4e5f-8a6b-7d2e1f0c3b4a")

    // Dispositivo
    const val DEVICE_NAME       = "YBY-WATCH"
    const val HARDWARE_ID       = "YBY-WATCH-001"
    const val PROTOCOL_VERSION  = 1
    const val MTU_TARGET        = 247

    // Intents
    object Intent {
        const val NONE            = 0x0000
        const val PING            = 0x0001
        const val GET_STATUS      = 0x0002
        const val GET_IDENTITY    = 0x0003
        const val SET_CONTEXT     = 0x0010
        const val CLEAR_CONTEXT   = 0x0011
        const val GET_CONTEXT     = 0x0012
        const val HAPTIC_PULSE    = 0x0020
        const val DISPLAY_MSG     = 0x0021
        const val CLEAR_MSG       = 0x0022
        const val SET_BRIGHTNESS  = 0x0023
        const val SYNC_TIME       = 0x0030
        const val SET_ALARM       = 0x0031
        const val CANCEL_ALARM    = 0x0032
        const val EXPORT_LOG      = 0x0040
        const val CLEAR_LOG       = 0x0041
        const val EXPORT_IDENTITY = 0x0042
        const val SAFE_MODE       = 0x00F0
        const val RESTART         = 0x00F1
        const val FACTORY_RESET   = 0x00FE
        const val SHUTDOWN        = 0x00FF
    }

    // Tipos de frame
    object FrameType {
        const val CMD       = 0x00
        const val EVENT     = 0x01
        const val TELEMETRY = 0x02
        const val ACK       = 0x03
        const val SYNC      = 0x04
        const val ERROR     = 0xFF
    }

    // Prioridades
    object Priority {
        const val P0 = 0x00
        const val P1 = 0x01
        const val P2 = 0x02
    }

    // Timeouts (ms)
    object Timeout {
        const val BLE_RECONNECT_BEACON = 30_000L
        const val OFFLINE_THRESHOLD    = 30_000L
        const val INTENT               = 5_000L
        const val THINK                = 10_000L
    }

    // Filas
    object Queue {
        const val P0_MAX = 10
        const val P1_MAX = 50
        const val P2_MAX = 100
    }
}
