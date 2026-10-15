---
id: CHG-005
title: Estado de contraparte para descubrimiento P0
doc_type: document_change
summary: Registrar que no existe actualmente un restaurante candidato sin inventar validación ni estado técnico.
updated_at: 2026-10-15
source_refs: [SRC-023]
incorporation_status: materializada_local
---

# CHG-005 — Estado de contraparte para descubrimiento P0

[← Cambios](README.md)

## Base, motivo, clasificación y alcance

Base local exacta: `15a563a8da0f4f81368183ad60eb1f2699b3b040`, que conserva sobre `main@4dba65591e1d4a2484c9d2267924c32420f7e744` la conciliación post-fusión de CHG-004. Rama: `codex/d3-espera-evidencia-p0`.

Clasificación: actualización factual de estado y planificación. Iván aclaró que no existe actualmente un restaurante candidato y que el proyecto sigue en fase de desarrollo. La primera parte determina que P0 no puede ejecutarse todavía; la segunda no demuestra que exista software implementado y no cambia los estados técnicos.

## Impacto documental

| Área/rutas | Estado | Motivo/evidencia |
| --- | --- | --- |
| `investigacion/SOURCE_REGISTER.md` | actualización realizada | Registrar `SRC-023`, autoridad, alcance y límite de la aclaración. |
| `negocio/BUSINESS_MODEL.md`, `decisiones/PENDING_DECISIONS.md`, `investigacion/GUIA_DESCUBRIMIENTO_P0.md` | actualización realizada | Mostrar que la guía está lista pero no existe contraparte seleccionada. |
| `planificacion/RISKS_AND_ASSUMPTIONS.md` | actualización realizada | Añadir el riesgo de prolongar hipótesis sin acceso a contexto real. |
| `README.md`, `planificacion/ROADMAP.md`, `gobierno/PROJECT_STATE.md` | actualización realizada | Separar preparación, espera de contraparte y evidencia técnica. |
| `planificacion/PROPUESTAS_FUTURAS.md` | actualización realizada | Registrar tercera observación local y condición cualitativa aún incumplida. |
| `trazabilidad/TRACEABILITY_MATRIX.md`, `trazabilidad/cambios/README.md`, `CHANGELOG.md` | actualización realizada | Enlazar el hecho, OBS-003 y su estado. |
| Requisitos, funcionalidades, arquitectura, SOP, pruebas y oferta | revisado sin modificación | La ausencia de contraparte no decide producto ni prueba implementación. |
| Privacidad, permisos y cumplimiento | revisado sin modificación | No existe tratamiento nuevo de datos ni contacto con participantes. |
| Procedimiento documental, validador, fixtures y workflow | revisado sin modificación | El circuito existente cubre el lote y no presenta un defecto nuevo. |
| FDA, Agent OS y otros repositorios | no aplicable / no modificados | Alcanzar tres observaciones no autoriza transferencia. |

## Dependencias, candidata y trabajo abierto

- Dependencias: [SRC-023](../../investigacion/SOURCE_REGISTER.md#src-023), [PD-003](../../decisiones/PENDING_DECISIONS.md#pd-003), [guía P0](../../investigacion/GUIA_DESCUBRIMIENTO_P0.md), [CHG-004](CHG-004-preparacion-descubrimiento-p0.md) y [PROP-001](../../planificacion/PROPUESTAS_FUTURAS.md#prop-001).
- Candidata sustantiva exacta: `9166899cbfc1d687f07606fb70b4c9217325ae33`, hija directa de la base local `15a563a8da0f4f81368183ad60eb1f2699b3b040`.
- Trabajo abierto: conseguir una contraparte real cuando sea oportuno; ejecutar la guía solo entonces; obtener juicio humano sobre utilidad y coste del circuito antes de reevaluar una transferencia.

## Validaciones y evidencias posteriores

Comprobaciones ejecutadas antes y repetidas sobre la candidata exacta `9166899cbfc1d687f07606fb70b4c9217325ae33` con árbol limpio:

| Control | Resultado | Límite |
| --- | --- | --- |
| `validate_docs.py` | `PASS`, 58 Markdown | Estructura y relaciones; no verifica la afirmación humana de forma independiente. |
| `test_validate_docs.py` | `PASS`, 24 mutaciones negativas y una autorización positiva | Rechazo/aceptación de los casos implementados. |
| `test_select_proposals.py` | `PASS` | Prueba el selector; no autoriza transferencia ni periodicidad. |
| `test_workflow_diff.py` | `PASS` | Ensayo Git local; no acredita CI nueva. |
| Carga YAML del workflow | `PASS` | Sintaxis local; el workflow no se modifica. |
| `git diff --check` | `PASS` | Limpieza mecánica del parche. |

## Revisión y costes observables

Revisión proporcional del autor. No se exige revisión independiente: el lote registra un hecho humano y propaga estado sin cambiar producto, arquitectura, privacidad, permisos, procedimiento crítico, gobierno, validador ni workflow. Tiempo humano no medido; coste/consumo no expuesto, `desconocido`.

## OBS-003 — Ausencia actual de restaurante candidato

| Aspecto | Observación | Resultado provisional |
| --- | --- | --- |
| Hecho nuevo | Iván indica que no existe actualmente un restaurante y que el proyecto está en desarrollo. | P0 queda preparado y a la espera de contraparte; no se inventa entrevista ni piloto. |
| Autoridad/alcance | Iván es responsable del proyecto; la afirmación describe disponibilidad de contraparte. | Se acepta como estado del proyecto, no como evidencia de implementación de software. |
| Impacto | Negocio, decisión pendiente, guía, riesgo, planificación y trazabilidad. | El circuito obliga a propagar el estado sin alterar requisitos o disponibilidad del producto. |
| Fricción | La solicitud de una entrevista presupuso una contraparte inexistente. | La continuidad debe ofrecer primero la opción “sin restaurante todavía” y no tratar P0 como bloqueo de todo trabajo conceptual. |
| Coste | Tiempo humano y consumo no medidos. | No existe base para concluir que el circuito compensa su coste en otro proyecto. |

## Evaluación provisional de D3

Con `OBS-001`, `OBS-002` y `OBS-003` se alcanza localmente la muestra cuantitativa mínima de tres cambios reales posteriores. La evidencia disponible permite una evaluación provisional:

- **Conservar:** procedimiento único, `CHG`, declaración de impacto, identidades exactas, validación local/CI y fusión humana separada.
- **Simplificar ya en la práctica:** no abrir PR exclusivas para conciliar una fusión; acumular esa corrección con el siguiente cambio real. Preferir hechos duraderos frente a frases transitorias de autorización.
- **No retirar todavía:** ninguna pieza ha mostrado fallo repetido suficiente; la muestra sigue siendo pequeña y dos observaciones son principalmente documentales.
- **No extender:** falta que el responsable humano documente si la utilidad justifica el coste; tampoco hay evidencia de necesidad equivalente en FDA u otro proyecto.

El mínimo numérico no completa por sí solo [PROP-001](../../planificacion/PROPUESTAS_FUTURAS.md#prop-001) ni autoriza reevaluación remota, transferencia o ejecución.

## Manifiesto exacto, DOC-GATE y siguiente acto condicionado

`DOC-GATE: PASSED` para la candidata exacta `9166899cbfc1d687f07606fb70b4c9217325ae33`. La revisión proporcional del autor y todas las comprobaciones exigibles pasaron; no existe revisión independiente porque no es exigible para este alcance. La identificación y cierre del gate se incorporan en un commit posterior de evidencia que no cambia `OBS-003` ni la evaluación provisional.

Siguiente acto de P0: esperar una contraparte real sin detener documentación conceptual autorizada. Siguiente decisión D3: Iván puede valorar si la utilidad observada justifica el coste; hasta entonces se conserva el circuito local y `PROP-001` permanece aplazada. Publicación o PR requieren autorización separada.
