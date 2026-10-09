# Eventos y métricas

[← Arquitectura](ARCHITECTURE.md) · [FEAT-001](../producto/funcionalidades/FEAT-001-gestion-tareas-servicio.md)

## Estado y límites

Contrato propuesto para demostrar trazabilidad del caso; su implementación no está acreditada. Medir lo operacionalmente relevante no significa grabar todo: se prefieren eventos estructurados y minimizados. Timestamps son del servidor en UTC; la zona del establecimiento sirve para presentar, no para ordenar.

## Sobre mínimo del evento

```text
event_id, event_type, event_version, occurred_at, recorded_at,
tenant_id, venue_id, correlation_id, causation_id,
actor_type, actor_id?, channel, entity_type, entity_id,
payload, schema_version
```

`actor_id` puede ser personal; su acceso y retención se gobiernan. `payload` no incluye transcripción completa salvo necesidad aprobada.

## Caso sintético de mesa 12

| Evento | Campos específicos |
| --- | --- |
| `service_request.received` | mesa, concepto bruto, party_size=3 |
| `service_request.clarification_requested` | campo=`quantity/unit` |
| `service_task.created` | quantity=1, unit=`basket`, priority=`normal`, idempotency_key |
| `service_task.offered` | cohort/policy_version; no lista completa si no es necesaria |
| `service_task.claim_attempted` | staff_id, expected_version |
| `service_task.claimed` | assignee_id, new_version |
| `service_task.claim_rejected` | reason=`already_claimed`; ganador solo si autorizado |
| `service_task.blocked` | reason, responsible_dependency? |
| `service_task.resumed` | resolution_ref |
| `service_task.completed` | completion_method, confirmer_id |

## Fórmulas candidatas

- Tiempo hasta claim = `claimed_at - created_at`.
- Tiempo de ejecución bruto = `completed_at - claimed_at`.
- Tiempo bloqueado = suma de intervalos `blocked → resumed`.
- Tiempo activo atribuible = ejecución bruta − bloqueos validados; no equivale por sí solo a rendimiento.
- Tiempo total cliente = `completed_at - request_received_at`.
- Duplicidad evitada = claims rechazados por `already_claimed`; no mide intentos fuera del sistema.

Los percentiles y comparaciones deben segmentar por tipo de tarea, turno, zona, carga, mesa, bloqueo y dependencia. No se publica un score individual compuesto hasta decidir fórmula, uso, auditabilidad y revisión jurídica.

## Calidad e interpretación

Cada métrica enlaza eventos fuente, versión de fórmula y ventanas. Retrasos de cocina, falta de recursos o conectividad no se imputan automáticamente al trabajador. Correcciones conservan el valor original y un evento de rectificación.
