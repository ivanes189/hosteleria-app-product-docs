---
id: FEAT-001
title: Gestión de tareas de servicio compartidas
doc_type: feature
summary: Crear, ofrecer, reclamar, ejecutar y cerrar solicitudes sin duplicidad.
updated_at: 2026-10-09
source_refs: [SRC-001]
related_decisions: [DEC-002, DEC-003]
dependencies: [FEAT-002, REQ-003, REQ-004]
design_status: en_evaluacion
implementation_status: desconocido
verification_status: no_verificado
availability_status: desconocida
incorporation_status: candidata_externa
---

# FEAT-001 — Gestión de tareas de servicio compartidas

[← Funcionalidades](README.md) · [SOP-001](../../operacion/procedimientos/SOP-001-atender-solicitud-servicio.md) · [TEST](../../validacion/TEST_SCENARIOS.md#test-001)

## Resumen, problema y beneficio

Una solicitud como “pan para la mesa 12” debe convertirse en una tarea visible, medible y con un único responsable. Iván pidió una solución eficiente, profesional y escalable que evite que dos empleados ejecuten la misma tarea. La aceptación atómica es la alternativa recomendada por la conversación, pero aún no tiene aprobación humana explícita.

## Actores y restricciones

Solicitante, personal elegible, encargado y sistema. La elegibilidad propuesta considera establecimiento, turno, rol/capacidad, zona, carga y permisos. Un LLM puede resolver intención y entidades; un servicio determinista debería validar permisos y transición. No se usa reconocimiento biométrico de voz por defecto: la identidad puede proceder de la sesión autenticada del dispositivo.

## Precondiciones y disparadores

- Mesa y establecimiento inequívocos.
- Cantidad confirmada cuando “para tres” no determine unidades.
- Sesión del personal autenticada y conectada.
- Evento de solicitud válido o creación autorizada por personal.

## Flujo principal propuesto — mesa 12

1. Se recibe “más pan para la mesa 12, somos tres”.
2. El sistema pregunta la cantidad si la regla no está aprobada; en el ejemplo sintético se confirma **una cesta**, no tres unidades.
3. Se crea una tarea `CREATED` con clave de idempotencia y timestamps del servidor.
4. El despachador obtiene personal elegible y ofrece/notifica de forma selectiva.
5. Elena dice “voy yo”. `ClaimTask(task_id, staff_id, expected_version)` intenta una transición atómica.
6. Si gana, la tarea queda `CLAIMED` por Elena y los demás canales actualizan su estado; si Carlos compite y pierde, recibe “Elena ya se ocupa”.
7. Elena confirma “pan de la doce servido”. Tras desambiguación contextual y validación, la tarea queda `COMPLETED`.

## Alternativas, errores y recuperación

- **Ambigüedad:** pedir mesa, objeto o cantidad; no crear tarea silenciosamente.
- **Mensaje repetido:** usar idempotencia y ventana/contexto, sin impedir una nueva solicitud legítima.
- **Sin claim:** caducar la oferta y ampliar candidatos o escalar al encargado; política pendiente.
- **Sin pan:** pasar a `BLOCKED` con motivo, crear o enlazar reposición y reanudar/reasignar al resolverse; detalle pendiente.
- **Desconexión:** el cliente conserva el intento local y reconcilia con el estado del servidor; no asume éxito.
- **Entrega no confirmada:** recordatorio o escalado proporcional; no marcar completada por mera expiración.

## Estados y transiciones

Propuesta mínima: `CREATED → OFFERED → CLAIMED → COMPLETED`, con `BLOCKED`, `CANCELLED`, `EXPIRED` y `REASSIGNED` por definir. La conversación propone para tareas simples una visión reducida `CREATED → CLAIMED → COMPLETED`. Ninguna máquina está aprobada como contrato técnico.

## Datos, eventos y dependencias

Campos candidatos: `task_id`, `venue_id`, `table_id`, `type`, `quantity`, `unit`, `priority`, `status`, `assignee_id`, `version`, `idempotency_key`, `blocked_reason` y timestamps. Contrato propuesto en [EVENTS_METRICS](../../arquitectura/EVENTS_METRICS.md).

## Métricas y aceptación

- Exactamente un claim exitoso ante dos intentos concurrentes.
- Estado consultable por personal autorizado sin exigir audio global.
- Tiempos de creación, oferta, claim y finalización calculables desde eventos inmutables.
- Bloqueos separados del tiempo imputable al trabajador.
- Nueva solicitud legítima después de una entrega no se elimina como duplicado.

## Evolución

- 2026-10-03: Iván plantea el problema de doble entrega y exige medición.
- 2026-10-03: el asistente propone propiedad y claim atómico.
- 2026-10-09: se documenta como diseño en evaluación; no se atribuye implementación.
