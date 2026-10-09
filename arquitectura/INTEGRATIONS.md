# Integraciones

[← Arquitectura](ARCHITECTURE.md)

## Estado

No hay evidencia accesible de integraciones de Hostelería App aprobadas o implementadas. Esta lista separa necesidades de elecciones.

| Integración | Finalidad | Estado | Riesgo/condición |
| --- | --- | --- | --- |
| TPV/POS | mesas, comandas, pagos | oportunidad | Contratos, idempotencia y proveedor por decidir. |
| KDS/cocina | `READY`, cursos, estaciones | oportunidad | No hacer depender seguridad alimentaria de inferencias. |
| Reservas | sesión/mesa/cliente | oportunidad | Minimización y reconciliación de identidad. |
| Dispositivos/PTT | audio del personal | en evaluación | Background, batería, higiene, ruido y privacidad. |
| Proveedor STT/TTS/Realtime | voz | en evaluación | Portabilidad, regiones, coste, retención y latencia. |
| Analítica/observabilidad | servicio y salud técnica | en evaluación | Separar telemetría técnica de métricas laborales. |

Los repositorios `voice-gateway`, `shared-libs` e `infra` prueban que existen patrones de integración, resiliencia y métricas en otro producto; no prueban compatibilidad de dominio ni despliegue actual.
