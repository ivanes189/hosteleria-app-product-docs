---
id: CHG-006
title: Cierre D3 del circuito de documentación viva
doc_type: document_change
summary: Registrar la decisión humana de conservar el circuito mínimo en Restaurant sin transferirlo ni automatizarlo.
updated_at: 2026-10-15
source_refs: [SRC-024, SRC-025]
incorporation_status: materializada_local
---

# CHG-006 — Cierre D3 del circuito de documentación viva

[← Cambios](README.md)

## Base, motivo, clasificación y alcance

Base local exacta: `32dcbb8f21c0e278015e2caac9f28725f7a18800`, conciliación post-fusión construida sobre `main@578bb5d5b2e3d9bec235b38f0ffe51c9eb41f2b8`. Rama: `codex/d3-cierre-evaluacion`.

Clasificación: decisión humana y cierre de evaluación documental. Iván confirmó la recomendación de conservar el circuito mínimo con las simplificaciones observadas, sin transferirlo a FDA ni automatizarlo todavía. El lote registra esa autoridad y cierra D3; no cambia el procedimiento, la política, el validador, el workflow ni el producto.

## Impacto documental

| Área/rutas | Estado | Motivo/evidencia |
| --- | --- | --- |
| `investigacion/SOURCE_REGISTER.md` | actualización realizada | Registrar `SRC-025`, autoridad y límites de la decisión humana. |
| `decisiones/DEC-005-cierre-d3-documentacion-viva.md`, `decisiones/DECISION_LOG.md` | actualización realizada | Conservar la decisión material y hacerla navegable. |
| `decisiones/DEC-004-documentacion-viva-minima.md` | actualización realizada | Enlazar el resultado del periodo de observación ordenado por la decisión original. |
| `README.md`, `planificacion/ROADMAP.md`, `gobierno/PROJECT_STATE.md` | actualización realizada | Marcar D3 completada y dejar P0 en espera de contraparte. |
| `planificacion/PROPUESTAS_FUTURAS.md` | actualización realizada | Reevaluar `PROP-001` y mantenerla aplazada; `PROP-004` no cambia. |
| `trazabilidad/TRACEABILITY_MATRIX.md`, `trazabilidad/cambios/README.md`, `CHANGELOG.md` | actualización realizada | Enlazar decisión, cambio, resultado y continuidad. |
| `AGENTS.md`, `DOCUMENTATION_POLICY.md`, `gobierno/PROCEDIMIENTO_DOCUMENTACION_VIVA.md` | revisado sin modificación | La decisión conserva los controles y solo aplica las simplificaciones prácticas ya documentadas. |
| Herramientas, fixtures y workflow documental | revisado sin modificación | No se detecta defecto ni se altera ninguna condición capaz de producir un falso `PASSED`. |
| Producto, arquitectura, requisitos, operación, privacidad, permisos, pruebas y oferta | revisado sin modificación | El cierre D3 no decide ni acredita producto. |
| FDA, Agent OS y otros repositorios | no aplicable / no modificados | La decisión excluye expresamente transferencia y trabajo remoto en esos repositorios. |

## Dependencias, candidata y trabajo abierto

- Dependencias: [DEC-004](../../decisiones/DEC-004-documentacion-viva-minima.md), [CHG-005](CHG-005-ausencia-restaurante-p0.md), [SRC-024](../../investigacion/SOURCE_REGISTER.md#src-024), [SRC-025](../../investigacion/SOURCE_REGISTER.md#src-025) y [PROP-001](../../planificacion/PROPUESTAS_FUTURAS.md#prop-001).
- Candidata sustantiva exacta: `b97928e4bf10ffb25b5e548f1524f6d247fae5ab`, hija directa de la conciliación local `32dcbb8f21c0e278015e2caac9f28725f7a18800`.
- Trabajo abierto: ninguno dentro de D3. P0 espera una futura contraparte real; cualquier transferencia o automatización requiere evidencia y autorización nuevas.

## Validaciones y evidencias posteriores

Comprobaciones ejecutadas antes y repetidas sobre la candidata exacta `b97928e4bf10ffb25b5e548f1524f6d247fae5ab` con árbol limpio:

| Control | Resultado | Límite |
| --- | --- | --- |
| `validate_docs.py` | `PASS`, 60 Markdown | Estructura y relaciones; no valida la conveniencia de la decisión. |
| `test_validate_docs.py` | `PASS`, 24 mutaciones negativas y una autorización positiva | Casos mecánicos del validador. |
| `test_select_proposals.py` | `PASS` | Selector local; no activa periodicidad. |
| `test_workflow_diff.py` | `PASS` | Ensayo Git local; no es CI remota. |
| Carga YAML del workflow | `PASS` | Sintaxis; el workflow no se modifica. |
| `git diff --check` | `PASS` | Limpieza mecánica. |

## Revisión y costes observables

Revisión proporcional del autor. No se exige revisión independiente: el lote registra una decisión humana y actualiza estado/relaciones sin cambiar producto, arquitectura, privacidad, permisos, procedimiento crítico, política, validador o workflow, ni relajar una condición del DOC-GATE. Tiempo humano no medido; coste/consumo no expuesto, `desconocido`.

## Resultado de D3

- **Conservar:** el circuito mínimo aplicado en Restaurant.
- **Simplificar:** agrupar conciliaciones post-fusión con el siguiente cambio real y evitar lenguaje transitorio cuando no aporte evidencia duradera.
- **Retirar o ampliar:** nada con la muestra actual.
- **Transferir o automatizar:** no; propuestas y autorizaciones continúan separadas.
- **Siguiente transición:** P0 cuando exista restaurante candidato y autoridad para el contacto; mientras tanto, no se inventa evidencia ni se adelanta P1.

## Manifiesto exacto, DOC-GATE y siguiente acto condicionado

`DOC-GATE: PASSED` para la candidata exacta `b97928e4bf10ffb25b5e548f1524f6d247fae5ab`. La decisión humana está clasificada, el impacto queda cubierto, la revisión proporcional y todas las comprobaciones exigibles pasaron. La identificación y cierre del gate se incorporan en un commit posterior de evidencia que no cambia `DEC-005` ni el resultado de D3.

Siguiente acto: esperar una contraparte real para P0 sin adelantar P1. Cualquier publicación o PR de este lote requiere autorización separada; transferencia y automatización permanecen fuera de alcance.
