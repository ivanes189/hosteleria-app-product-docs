---
id: DEC-004
title: Circuito mínimo de documentación viva
doc_type: decision
summary: Conciliar Restaurant, probar un circuito documental pequeño y extender solo lo útil.
decision_date: 2026-10-15
updated_at: 2026-10-15
source_refs: [SRC-015, SRC-019, SRC-025]
design_status: aprobado
incorporation_status: integrada
---

# DEC-004 — Circuito mínimo de documentación viva

[← Registro](DECISION_LOG.md)

## Contexto y autoridad

Iván aceptó la dirección del traspaso y autorizó preparación local, herramientas documentales, pruebas, una rama y commits candidatos. Esa autorización inicial no incluía publicación, PR, fusión, automatizaciones ni cambios remotos de permisos o protecciones.

## Decisión

Conciliar primero el estado documental de Restaurant Operations OS; implantar después un circuito mínimo para registrar impacto, decisiones y propuestas; probarlo con pocos cambios y medir su coste observable. Solo se extenderán las piezas que demuestren utilidad.

FDA aporta métodos o componentes seleccionados, pero conserva su repositorio y autoridad. Agent OS conserva su función de plataforma de agentes de negocio y no coordina este desarrollo documental. Ninguno es prerrequisito para comenzar el descubrimiento del restaurante.

## Consecuencias y límites

- Se amplían el `CHG`, el registro de reutilización, la política y los validadores existentes; no se duplican registros.
- Scripts verifican estructura; IA interpreta impacto; decisiones y revisiones humanas conservan su autoridad.
- Una condición de revisión cumplida no autoriza una propuesta ni su ejecución.
- No se resuelven nombre, claim atómico, MVP, jurisdicción, precio ni otras decisiones de producto pendientes.
- La transferencia a FDA u otro proyecto será un encargo separado y condicionado a evidencia de utilidad.

Una autorización posterior permitió publicar y abrir la PR #1; Iván realizó la fusión. La decisión está `integrada` en `main@a8365b6674381c4c23985bdce4a58a178c5c4a69`. Esto no autoriza por sí solo automatización periódica, transferencia a otros proyectos ni decisiones de producto.

El periodo de observación posterior concluye en [DEC-005](DEC-005-cierre-d3-documentacion-viva.md): el circuito se conserva en Restaurant con dos simplificaciones prácticas, pero no se transfiere ni automatiza todavía.
