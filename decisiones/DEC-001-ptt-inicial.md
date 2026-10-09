---
id: DEC-001
title: PTT como interacción de voz inicial
doc_type: decision
summary: Empezar con push-to-talk y preservar evolución a activación por voz.
decision_date: 2026-10-03
updated_at: 2026-10-09
source_refs: [SRC-001]
design_status: aprobado
incorporation_status: candidata_externa
---

# DEC-001 — PTT como interacción de voz inicial

[← Registro](DECISION_LOG.md)

**Decisión humana:** empezar con push-to-talk. La arquitectura debe facilitar una evolución futura a activación por voz, posiblemente con reconocimiento, sin seleccionar aún mecanismo o proveedor.

**Motivo:** reducir fricción y riesgos del primer producto, manteniendo una ruta manos libres futura. **Consecuencias:** voz es un adaptador de entrada; pantalla y voz deben converger en comandos comunes; no se aprueba escucha continua ni biometría vocal. **Pendiente:** wake word local/cloud, hardware, plataformas, retención y SLO.
