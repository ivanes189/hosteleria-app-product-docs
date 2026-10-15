---
id: CHG-002
title: Conciliación y circuito mínimo de documentación viva
doc_type: document_change
summary: Actualizar el estado publicado, implantar el circuito mínimo y ensayarlo localmente.
updated_at: 2026-10-15
source_refs: [SRC-014, SRC-015, SRC-016]
incorporation_status: materializada_local
---

# CHG-002 — Conciliación y circuito mínimo de documentación viva

[← Cambios](README.md)

## Base, motivo, clasificación y alcance

Base exacta: `main@e35481da2a99e9a9546664712569c27b70010a69`, árbol local limpio al inicio. Rama: `codex/documentacion-viva-piloto`. Clasificación: corrección factual de estado, decisión de gobierno y herramienta documental; no incluye código de producto.

La secuencia autorizada tiene tres resultados dependientes dentro de un único expediente: L1 concilia publicación y cierre; L2 implanta el circuito mínimo sobre L1; P1 ensaya el conjunto. Separarlos en expedientes no produciría resultados independientes y fragmentaría la revisión. Ningún resultado se presenta como aprobado o integrado antes de tiempo.

## Impacto documental

| Área/rutas | Estado | Motivo/evidencia |
| --- | --- | --- |
| `README.md`, `gobierno/PROJECT_STATE.md`, `planificacion/ROADMAP.md` | actualización realizada en L1 | Sustituir el estado anterior a la publicación por hechos del informe original y la lectura pública actual. |
| `gobierno/HISTORIAL_PUBLICACION_INICIAL.md`, `gobierno/CANDIDATE_MANIFEST.md` | actualización realizada en L1 | Hacer navegables cierre/publicación y preservar el manifiesto como instantánea. |
| `decisiones/DEC-004-*`, `DECISION_LOG.md` | actualización realizada en L1 | Capturar la aceptación de Iván sin convertir pendientes de producto en decisiones. |
| `investigacion/SOURCE_REGISTER.md`, `REUSE_REGISTER.md` | actualización realizada en L1 | Registrar procedencia, selección acotada, versiones, límites y precisión factual de RU-007. |
| Política, instrucciones, procedimiento, propuestas y herramientas | pendiente L2 | Implantar el circuito y sus controles sobre la candidata conciliada. |
| Piloto y medición | pendiente P1 | Ejecutar de tres a cinco casos pertinentes, incluidos negativos solo en fixtures/copias temporales. |
| Producto, arquitectura, operación, privacidad y permisos | revisado sin modificación en L1 | La conciliación no aporta evidencia para cambiar su estado. |
| FDA, Agent OS y repositorios fuente | no aplicable / no modificados | Permanecen en solo lectura y con autorización independiente. |
| GitHub remoto | revisado sin modificación | Consulta pública únicamente; no se hizo `fetch`, `pull`, push, PR, fusión ni cambio de controles. |

## Candidatas y dependencia

| Candidata | Contenido | Identidad | Estado |
| --- | --- | --- | --- |
| Inicial | 49 entradas históricas | `e35481da2a99e9a9546664712569c27b70010a69` y manifiesto externo `8e003c…` | integrada; C2 `APTO`, DOC-GATE `PASSED` según cierre original. |
| L1 | conciliación documental | commit local con asunto `docs: reconcile initial publication state` | se identificará al crear el commit; no hereda el dictamen inicial. |
| L2/P1 | circuito y piloto | commit local final del expediente | pendiente. |

## Validaciones y evidencia

La base inicial se revalidó antes de editar: `validate_docs.py` PASS (45 Markdown), diez fixtures negativos PASS, `git diff --check` PASS, SHA-256 externo del manifiesto coincidente y 49 huellas PASS. La consulta pública observó repositorio/commit/rama, cero PR, ausencia de workflows y protección visible; los detalles autenticados quedaron limitados por la credencial `gh` inválida.

L1 pasa `python3 -B herramientas/validate_docs.py` (48 Markdown), los diez fixtures negativos de `test_validate_docs.py` y `git diff --check`. Regenerar el manifiesto inicial no forma parte de esas comprobaciones. Las comprobaciones de L2/P1 se registrarán sobre su candidata exacta.

## Revisión, DOC-GATE y siguiente acto

La revisión propia durante la preparación es interna, no independiente. L1 permanece `OPEN` mientras L2/P1 siga dentro del alcance declarado. Al terminar se aplicará la revisión exigible a la candidata exacta y se registrarán revisor, hallazgos, ciclo y coste observable o `desconocido`.

`DOC-GATE: OPEN`. Siguiente acto: completar L2 y P1 localmente; después identificar el commit exacto y solicitar solo la autorización remota o revisión que corresponda. Publicar una rama que contiene un workflow puede activarlo y requiere autorización explícita.
