---
id: SUB-001
title: Coordinación conversacional del personal
doc_type: subproduct
summary: Oportunidad de oferta para coordinación por voz y estado compartido.
updated_at: 2026-10-09
source_refs: [SRC-001]
related_features: [FEAT-001, FEAT-002]
design_status: propuesto
implementation_status: desconocido
verification_status: no_verificado
availability_status: desconocida
incorporation_status: candidata_externa
---

# SUB-001 — Coordinación conversacional del personal

[← Subproductos](README.md)

**Categoría:** oportunidad de subproducto; no oferta aprobada. **Necesidad:** coordinar sala, runners, cocina y barra sin obligar a consultar continuamente una pantalla. **Clientes/usuarios:** establecimientos de hostelería y su personal, por validar.

Funcionaría sobre tareas compartidas, notificación selectiva, PTT y consulta de contexto. Entradas: solicitudes, eventos operativos y comandos autorizados. Salidas: tareas, estados, avisos, evidencias y métricas. Depende de identidad del dispositivo, permisos, núcleo determinista, voz, observabilidad, multi-tenancy y operación segura.

Ventajas hipotéticas: menos duplicidades, menor tiempo de coordinación y trazabilidad. No hay evidencia accesible de ventajas medidas, pilotos, precio, coste, soporte o modalidad comercial. Riesgos: ruido de notificaciones, vigilancia desproporcionada, latencia, falsas interpretaciones, dependencia de red y hardware, rechazo del personal.

Métricas de valor propuestas: duplicidades evitadas, tiempo hasta claim, tiempo total contextualizado, tareas abandonadas, interrupciones por trabajador/hora y satisfacción de personal/cliente. Ninguna debe usarse aisladamente para decisiones laborales.

**Evolución:** validar problema y aceptabilidad → decidir MVP → piloto con DPIA y reglas humanas → evaluar oferta. No se presenta como `Staff Copilot` definitivo hasta resolver taxonomía y marca.
