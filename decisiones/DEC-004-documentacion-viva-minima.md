---
id: DEC-004
title: Circuito mínimo de documentación viva
doc_type: decision
summary: Conciliar Restaurant, probar un circuito documental pequeño y extender solo lo útil.
decision_date: 2026-10-15
updated_at: 2026-10-15
source_refs: [SRC-015]
design_status: aprobado
incorporation_status: materializada_local
---

# DEC-004 — Circuito mínimo de documentación viva

[← Registro](DECISION_LOG.md)

## Contexto y autoridad

Iván aceptó la dirección del traspaso y autorizó preparación local, herramientas documentales, pruebas, una rama y commits candidatos. La autorización no incluye publicación, PR, fusión, automatizaciones ni cambios remotos de permisos o protecciones.

## Decisión

Conciliar primero el estado documental de Restaurant Operations OS; implantar después un circuito mínimo para registrar impacto, decisiones y propuestas; probarlo con pocos cambios y medir su coste observable. Solo se extenderán las piezas que demuestren utilidad.

FDA aporta métodos o componentes seleccionados, pero conserva su repositorio y autoridad. Agent OS conserva su función de plataforma de agentes de negocio y no coordina este desarrollo documental. Ninguno es prerrequisito para comenzar el descubrimiento del restaurante.

## Consecuencias y límites

- Se amplían el `CHG`, el registro de reutilización, la política y los validadores existentes; no se duplican registros.
- Scripts verifican estructura; IA interpreta impacto; decisiones y revisiones humanas conservan su autoridad.
- Una condición de revisión cumplida no autoriza una propuesta ni su ejecución.
- No se resuelven nombre, claim atómico, MVP, jurisdicción, precio ni otras decisiones de producto pendientes.
- La transferencia a FDA u otro proyecto será un encargo separado y condicionado a evidencia de utilidad.

La incorporación de esta decisión permanece `materializada_local` hasta una publicación y fusión autorizadas.
