---
id: CHG-004
title: Preparación mínima del descubrimiento P0
doc_type: document_change
summary: Convertir las preguntas de PD-003 en un instrumento ejecutable sin inventar evidencia de restaurante.
updated_at: 2026-10-15
source_refs: [SRC-001, SRC-015, SRC-022]
incorporation_status: en_pr
---

# CHG-004 — Preparación mínima del descubrimiento P0

[← Cambios](README.md)

## Base, motivo, clasificación y alcance

Base local exacta: `92669a9059de5ea21c3348555b2400e7a9a2e188`, que conserva sobre `main@0478a8e7fc6ab799b4af1876a421bc532424133b` la conciliación post-fusión de CHG-003. Rama: `codex/documentacion-viva-d3-continuidad`.

Clasificación: preparación de investigación de producto y cambio documental; no decide MVP, no añade requisitos, no cambia privacidad/permisos y no ejecuta entrevistas. La carencia concreta es que [BUSINESS_MODEL](../../negocio/BUSINESS_MODEL.md#descubrimiento-del-primer-restaurante) enumera preguntas, pero no ofrece un recorrido reproducible, una baseline mínima ni una ficha de salida segura para un repositorio público.

## Impacto documental

| Área/rutas | Estado | Motivo/evidencia |
| --- | --- | --- |
| `investigacion/GUIA_DESCUBRIMIENTO_P0.md` | actualización realizada | Instrumento único para sesión, baseline, síntesis y criterio de salida. |
| `negocio/BUSINESS_MODEL.md`, `decisiones/PENDING_DECISIONS.md` | actualización realizada | Enlazar PD-003 y sus preguntas con la ejecución, sin resolverlas. |
| `planificacion/RISKS_AND_ASSUMPTIONS.md` | actualización realizada | Registrar el riesgo de publicar notas o datos sensibles en un repositorio público. |
| `investigacion/SOURCE_REGISTER.md` | actualización realizada en la evidencia de publicación | Registrar autorización, candidata y PR sin ampliar permisos. |
| `README.md`, `planificacion/ROADMAP.md`, `gobierno/PROJECT_STATE.md` | actualización realizada | Hacer navegable la guía y separar preparación local de validación real. |
| `planificacion/PROPUESTAS_FUTURAS.md` | actualización realizada | Registrar `OBS-002` como segundo uso del circuito, todavía insuficiente para `PROP-001`. |
| `trazabilidad/TRACEABILITY_MATRIX.md`, `trazabilidad/cambios/README.md`, `CHANGELOG.md` | actualización realizada | Enlazar PD-003, guía, estado e historia. |
| Requisitos, funcionalidades, SOP, pruebas y oferta | revisado sin modificación | No existe nueva evidencia ni decisión humana que permita cambiar su contenido. |
| Privacidad, permisos y cumplimiento | revisado sin modificación | La guía aplica límites vigentes; no decide jurisdicción, base jurídica, consentimiento o DPIA. |
| Procedimiento documental, validador, fixtures y workflow | revisado sin modificación | El circuito existente cubre el lote; no se observó un defecto mecánico. |
| FDA, Agent OS y otros repositorios | no aplicable / no modificados | D3 y `PROP-001` no autorizan transferencia. |

## Dependencias, candidata y trabajo abierto

- Dependencias: [PD-003](../../decisiones/PENDING_DECISIONS.md#pd-003), [PD-004](../../decisiones/PENDING_DECISIONS.md#pd-004), [REQ-011](../../requisitos/REQUIREMENTS.md#req-011), [BUSINESS_MODEL](../../negocio/BUSINESS_MODEL.md) y [CHG-003](CHG-003-observacion-d3-1.md).
- Candidata sustantiva exacta: `f395a125694a7b835143f7b231279a7b3f54a6fd`, hija directa de la base local `92669a9059de5ea21c3348555b2400e7a9a2e188`.
- Trabajo abierto: selección humana del restaurante, autorización de contacto y destino de notas; ejecución de la guía; incorporación posterior de evidencia real y decisiones resultantes.

## Validaciones y evidencias posteriores

Comprobaciones ejecutadas antes y repetidas sobre la candidata exacta `f395a125694a7b835143f7b231279a7b3f54a6fd` con árbol limpio:

| Control | Resultado | Límite |
| --- | --- | --- |
| `validate_docs.py` | `PASS`, 57 Markdown | Estructura y relaciones; no verdad ni suficiencia de la guía. |
| `test_validate_docs.py` | `PASS`, 24 mutaciones negativas y una autorización positiva | Rechazo/aceptación de los casos implementados. |
| `test_select_proposals.py` | `PASS` | Prueba el selector; no activa periodicidad. |
| `test_workflow_diff.py` | `PASS` | Ensayo Git local; no acredita CI nueva. |
| Carga YAML del workflow | `PASS` | Sintaxis local; el workflow no se modifica. |
| `git diff --check` | `PASS` | Limpieza mecánica del parche. |

## Revisión y costes observables

Revisión proporcional del autor. No se exige revisión independiente: la candidata prepara captura de evidencia y aplica límites ya vigentes, pero no modifica producto, arquitectura, privacidad, permisos, procedimiento crítico, gobierno, validador ni workflow. Tiempo humano no medido; coste/consumo no expuesto, `desconocido`.

## OBS-002 — Instrumento de descubrimiento

| Aspecto | Observación | Resultado provisional |
| --- | --- | --- |
| Necesidad real | P0 requiere evidencia de restaurante; las preguntas existían, pero no un formato de ejecución y salida. | La guía cubre la carencia sin duplicar el modelo de negocio ni crear un almacén de entrevistas. |
| Impacto | Negocio, decisión pendiente, riesgo, planificación y trazabilidad; ningún estado positivo de producto. | La matriz de impacto mantuvo separados preparación, evidencia y decisión. |
| Fricción | La evidencia sensible no puede conservarse por defecto en este repositorio público. | La guía exige destino humano autorizado y solo síntesis minimizada en el repositorio. |
| Coste | Tiempo humano y uso de la futura sesión aún desconocidos. | No existe base para afirmar ahorro o utilidad sostenida. |

`OBS-002` es el segundo cambio real observado por D3 y el primero orientado directamente a preparación de producto. No satisface por sí solo `PROP-001`: falta al menos otro cambio real, ausencia de omisiones críticas y justificación humana de utilidad frente al coste.

## Manifiesto exacto, DOC-GATE y siguiente acto condicionado

`DOC-GATE: PASSED` para la candidata exacta `f395a125694a7b835143f7b231279a7b3f54a6fd`. La revisión proporcional del autor y todas las comprobaciones exigibles pasaron; no existe revisión independiente porque no es exigible para este alcance. La identificación y cierre del gate se incorporan en un commit posterior de evidencia que no cambia la guía ni `OBS-002`.

Tras [autorización expresa](../../investigacion/SOURCE_REGISTER.md#src-022), la rama se publicó y se abrió la [PR #4](https://github.com/ivanes189/hosteleria-app-product-docs/pull/4); la fusión sigue reservada al acto humano separado. El siguiente acto de producto permanece pendiente: una persona responsable selecciona el restaurante y autoriza contacto y manejo de notas. No se activan automatizaciones ni trabajos en otros repositorios.
