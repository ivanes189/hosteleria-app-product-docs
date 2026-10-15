---
id: CHG-002
title: Conciliación y circuito mínimo de documentación viva
doc_type: document_change
summary: Actualizar el estado publicado, implantar el circuito mínimo y ensayarlo localmente.
updated_at: 2026-10-15
source_refs: [SRC-014, SRC-015, SRC-016, SRC-017, SRC-018]
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
| `AGENTS.md`, `DOCUMENTATION_POLICY.md`, `gobierno/PROCEDIMIENTO_DOCUMENTACION_VIVA.md`, plantilla `CHG` y [paquete de revisión](../../gobierno/revisiones/PAQUETE_REVISION_CHG-002.md) | actualización realizada en L2 y preparación de revisión | Punto de entrada breve, procedimiento único, impacto obligatorio, revisión y límites de automatización; activación interna de la revisora independiente sin tarea manual separada. |
| `planificacion/PROPUESTAS_FUTURAS.md`, planificación y trazabilidad | actualización realizada en L2 | Registro único `PROP`, cuatro propuestas concretas y estados/autorización separados. |
| `herramientas/`, `.github/workflows/documentation.yml` | actualización realizada en L2 | Parser simple, selección idempotente, fixtures y candidata de CI con lectura mínima y acción fijada. |
| `negocio/BUSINESS_MODEL.md`, `decisiones/PENDING_DECISIONS.md` | actualización realizada en L2 | Preguntas e hipótesis de descubrimiento sin inventar cliente, demanda, precio, coste o resultado. |
| Piloto y medición | actualización realizada en P1 | Cinco casos pertinentes; defectos deliberados solo en copias temporales. Resultados abajo. |
| Producto, arquitectura, operación, privacidad y permisos | revisado sin modificación en L1 | La conciliación no aporta evidencia para cambiar su estado. |
| FDA, Agent OS y repositorios fuente | no aplicable / no modificados | Permanecen en solo lectura y con autorización independiente. |
| GitHub remoto | revisado sin modificación | Consulta pública únicamente; no se hizo `fetch`, `pull`, push, PR, fusión ni cambio de controles. |

## Candidatas y dependencia

| Candidata | Contenido | Identidad | Estado |
| --- | --- | --- | --- |
| Inicial | 49 entradas históricas | `e35481da2a99e9a9546664712569c27b70010a69` y manifiesto externo `8e003c…` | integrada; C2 `APTO`, DOC-GATE `PASSED` según cierre original. |
| L1 | conciliación documental | `97a6551449b8cefe441d7116c604adcbf185abec` | materializada localmente; no hereda el dictamen inicial. |
| L2/P1 | circuito y piloto | commit local con asunto `docs: add living documentation circuit` | candidata preparada; hash se obtiene de la rama tras crear el commit. |

## Validaciones y evidencia

La base inicial se revalidó antes de editar: `validate_docs.py` PASS (45 Markdown), diez fixtures negativos PASS, `git diff --check` PASS, SHA-256 externo del manifiesto coincidente y 49 huellas PASS. La consulta pública observó repositorio/commit/rama, cero PR, ausencia de workflows y protección visible; los detalles autenticados quedaron limitados por la credencial `gh` inválida.

L1 pasa `python3 -B herramientas/validate_docs.py` (48 Markdown), los diez fixtures negativos de `test_validate_docs.py` y `git diff --check`.

L2/P1 pasa en local:

| Control | Resultado | Límite |
| --- | --- | --- |
| `validate_docs.py` | `PASS`, 51 Markdown | estructura/relaciones; no verdad o suficiencia. |
| `test_validate_docs.py` | `PASS`, 16 mutaciones negativas | incluye ID/estado/condición/autorización `PROP`, impacto `CHG` y pin de action. |
| `test_select_proposals.py` | `PASS` | fecha, evento, evidencia, unicidad, checkpoint y cambio de evidencia. |
| Ensayo CLI con checkpoint temporal | primera salida `PROP-001: evento,evidencia_nueva`; segunda `NO_SELECTION` | no es una automatización activada ni una política de notificación. |
| Workflow YAML y `git diff --check` | `PASS` | sintaxis local; GitHub Actions no lo ha ejecutado. |

Regenerar el manifiesto inicial no forma parte de estas comprobaciones. El workflow usa solo `pull_request`, `contents: read`, no secretos, `persist-credentials: false`, nombre estable `documentation / validate` y `actions/checkout` v7.0.1 fijada a `3d3c42e5aac5ba805825da76410c181273ba90b1` según [SRC-017](../../investigacion/SOURCE_REGISTER.md#src-017).

## Piloto y medición

| Caso | Tipo y evidencia | Resultado |
| --- | --- | --- |
| PIL-01 | Editorial: `Destino previsto` pasó a `Destino documental` tras publicarse el repositorio. | Cambio proporcional, sin alterar una decisión. |
| PIL-02 | Factual/material: publicación inicial y precisión de RU-007 conciliadas con informe y rutas exactas. | Propagó estado, fuente, historial, roadmap y trazabilidad; detectó el riesgo de sobrescribir el manifiesto histórico. |
| PIL-03 | Propuesta aplazada: `PROP-001` reevaluada por evento/evidencia local. | El selector la encontró, pero la conclusión sigue siendo esperar porque faltan cambios reales y utilidad sostenida. |
| PIL-04 | Decisión conversacional: [DEC-004](../../decisiones/DEC-004-documentacion-viva-minima.md) capturada sin PR de código. | Autoridad, límites y pendientes quedaron navegables sin aprobar decisiones de producto. |
| PIL-05 | Ensayo sintético entre repositorios: código hipotético aún propuesto frente a documentación local. | El procedimiento exige repositorio/commit o PR, versión, pruebas, responsable y pendiente de sincronización; no se creó repositorio ficticio ni se afirmó implementación. Control semántico manual, no validación automática. |

Tiempo humano: no medido. Coste/consumo de herramientas y revisión: `desconocido`, no expuesto. No se infiere ahorro ni baseline retrospectiva de esta muestra.

Se conservan el procedimiento único, `CHG`, `PROP` plano, validador y fixtures. Se omiten por ahora skill de Codex, dashboard, base de datos, revisor IA y programación periódica. Los controles mecánicos funcionan en local; falta observar fricción en cambios reales, ejecutar CI en GitHub y realizar la revisión independiente.

## Revisión, DOC-GATE y siguiente acto

La revisión propia durante la preparación es interna, no independiente. Al cambiar política y validador de forma que podrían permitir un falso `PASSED`, la candidata completa requiere revisión independiente en contexto nuevo. [SRC-018](../../investigacion/SOURCE_REGISTER.md#src-018) fija que el coordinador active dentro de esta misma tarea una única instancia GPT-6 Astra, con razonamiento alto y solo lectura; esa instancia no modifica la candidata y conserva la continuidad en eventuales revalidaciones C1/C2. Aún no se ha emitido dictamen: no hay C1 abierto y el coste es `desconocido`.

`DOC-GATE: OPEN` por revisión independiente pendiente. Siguiente acto: fijar el SHA y el rango exactos en el [paquete preparado](../../gobierno/revisiones/PAQUETE_REVISION_CHG-002.md), activar internamente la revisora configurada y registrar su dictamen y eventuales ciclos. Solo tras un resultado apto se solicitará autorización para publicar la rama y abrir PR. Publicar esta rama y abrir la PR puede ejecutar el workflow preparado; no está autorizado todavía. Cambiar protecciones o fusionar requerirá permisos separados.
