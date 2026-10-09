---
id: DEC-003
title: Claim atómico para tareas compartidas
doc_type: decision
summary: Propuesta para que solo una persona reclame una tarea concurrente.
decision_date: null
updated_at: 2026-10-09
source_refs: [SRC-001]
design_status: propuesto
incorporation_status: candidata_externa
---

# DEC-003 — Claim atómico para tareas compartidas

[← Registro](DECISION_LOG.md)

**Propuesta de IA, no aprobada:** cada tarea compartida admite un único cambio atómico de disponible a reclamada, usando versión esperada o mecanismo equivalente. El ganador recibe confirmación y el resto ve el nuevo responsable.

**Alternativas consideradas en la conversación:** rangos fijos de mesas; comprobar manualmente si otro ya atendió; difundir avisos a todos. La propuesta atómica reduce duplicidad y no obliga a desplazarse para comprobar, pero necesita conectividad, reconciliación offline, idempotencia y política de reasignación.

**Condición de aprobación:** Iván elige esta regla y se detallan estados, expiración, bloqueo, autoridad de reasignación y experiencia ante desconexión.
