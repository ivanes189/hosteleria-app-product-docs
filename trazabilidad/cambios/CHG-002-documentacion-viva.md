---
id: CHG-002
title: Conciliación y circuito mínimo de documentación viva
doc_type: document_change
summary: Actualizar el estado publicado, implantar el circuito mínimo y ensayarlo localmente.
updated_at: 2026-10-15
source_refs: [SRC-014, SRC-015, SRC-016, SRC-017, SRC-018, SRC-019]
incorporation_status: integrada
---

# CHG-002 — Conciliación y circuito mínimo de documentación viva

[← Cambios](README.md)

## Base, motivo, clasificación y alcance

Base exacta: `main@e35481da2a99e9a9546664712569c27b70010a69`, árbol local limpio al inicio. Rama: `codex/documentacion-viva-piloto`. Clasificación: corrección factual de estado, decisión de gobierno y herramienta documental; no incluye código de producto.

La secuencia autorizada tiene tres resultados dependientes dentro de un único expediente: L1 concilia publicación y cierre; L2 implanta el circuito mínimo sobre L1; P1 ensaya el conjunto. Separarlos en expedientes no produciría resultados independientes y fragmentaría la revisión. Ningún resultado se presenta como aprobado o integrado antes de tiempo.

## Impacto documental

| Área/rutas | Estado | Motivo/evidencia |
| --- | --- | --- |
| `README.md`, `gobierno/PROJECT_STATE.md`, `planificacion/ROADMAP.md` | actualización realizada en L1 y cierre post-fusión | Sustituir estados históricos por hechos verificados y señalar D3 sin adelantar sus resultados. |
| `gobierno/HISTORIAL_PUBLICACION_INICIAL.md`, `gobierno/CANDIDATE_MANIFEST.md` | actualización realizada en L1 | Hacer navegables cierre/publicación y preservar el manifiesto como instantánea. |
| `decisiones/DEC-004-*`, `DECISION_LOG.md` | actualización realizada en L1 y cierre post-fusión | Capturar la aceptación de Iván y reflejar incorporación sin convertir pendientes de producto en decisiones. |
| `investigacion/SOURCE_REGISTER.md`, `REUSE_REGISTER.md` | actualización realizada en L1; SRC-019 ampliada al cierre | Registrar procedencia, selección acotada, versiones, límites y evidencia remota de incorporación. |
| `AGENTS.md`, `DOCUMENTATION_POLICY.md`, `gobierno/PROCEDIMIENTO_DOCUMENTACION_VIVA.md`, plantilla `CHG`, [paquete](../../gobierno/revisiones/PAQUETE_REVISION_CHG-002.md) y dictámenes [C0](../../gobierno/revisiones/DICTAMEN_CHG-002-C0.md)/[C1](../../gobierno/revisiones/DICTAMEN_CHG-002-C1.md)/[C2](../../gobierno/revisiones/DICTAMEN_CHG-002-C2.md) | actualización realizada; cierre local | Punto de entrada breve, procedimiento único, impacto obligatorio, candidatas/dictámenes preservados y ciclos continuos hasta `APTO`. |
| `planificacion/PROPUESTAS_FUTURAS.md`, planificación y trazabilidad | actualización realizada en L2 | Registro único `PROP`, cuatro propuestas concretas y estados/autorización separados. |
| `herramientas/`, `.github/workflows/documentation.yml` | actualización realizada en L2 y corrección C1 | Parser/relaciones `PROP`, memoria idempotente, fixtures y diff explícito base…candidata en la CI preparada, con lectura mínima y acción fijada. |
| `negocio/BUSINESS_MODEL.md`, `decisiones/PENDING_DECISIONS.md` | actualización realizada en L2 | Preguntas e hipótesis de descubrimiento sin inventar cliente, demanda, precio, coste o resultado. |
| Piloto y medición | actualización realizada en P1 | Cinco casos pertinentes; defectos deliberados solo en copias temporales. Resultados abajo. |
| Producto, arquitectura, operación, privacidad y permisos | revisado sin modificación en L1 | La conciliación no aporta evidencia para cambiar su estado. |
| FDA, Agent OS y repositorios fuente | no aplicable / no modificados | Permanecen en solo lectura y con autorización independiente. |
| GitHub remoto | integrada por decisión humana | [PR #1](https://github.com/ivanes189/hosteleria-app-product-docs/pull/1) fusionada por Iván; check final `PASS`; merge squash `a8365b66…` con árbol idéntico al head. Controles consultados sin modificarlos. |

## Candidatas y dependencia

| Candidata | Contenido | Identidad | Estado |
| --- | --- | --- | --- |
| Inicial | 49 entradas históricas | `e35481da2a99e9a9546664712569c27b70010a69` y manifiesto externo `8e003c…` | integrada; C2 `APTO`, DOC-GATE `PASSED` según cierre original. |
| L1 | conciliación documental | `97a6551449b8cefe441d7116c604adcbf185abec` | materializada localmente; no hereda el dictamen inicial. |
| L2/P1/C0 | circuito, piloto y regla operativa de revisión | `36d071fb231bb2dd13b1dcc2c0c88305c41f2de0` | revisión completa `NO APTO`; preservada; C1 abierto. |
| C1 | corrección exclusiva de `CHG002-RI-001` a `CHG002-RI-004` y efectos directos | `e86f3674ae46f8514d8844321c4b52f8de3f98f9` | revalidación `NO APTO`: RI-001/003/004 resueltos; remanente RI-002 preservado; C2 abierto. |
| C2 | correspondencia canónica exigida por el remanente `CHG002-RI-002` | `4246943b9ef288e0a437819d89934e2c08e634f4` | revalidación `APTO`; cuatro hallazgos resueltos; C1/C2 consumidos, sin C3. |
| Incorporación | rama y evidencias de cierre | head `5b7c5e90901f753ffdebc47a9443ba0cfe1b49b8` → squash `main@a8365b6674381c4c23985bdce4a58a178c5c4a69` | integrada; árboles idénticos; no altera el SHA exacto al que se refiere el dictamen C2. |

## Validaciones y evidencia

La base inicial se revalidó antes de editar: `validate_docs.py` PASS (45 Markdown), diez fixtures negativos PASS, `git diff --check` PASS, SHA-256 externo del manifiesto coincidente y 49 huellas PASS. La consulta pública observó repositorio/commit/rama, cero PR, ausencia de workflows y protección visible; los detalles autenticados quedaron limitados por la credencial `gh` inválida.

L1 pasa `python3 -B herramientas/validate_docs.py` (48 Markdown), los diez fixtures negativos de `test_validate_docs.py` y `git diff --check`.

L2/P1 pasa en local:

| Control | Resultado | Límite |
| --- | --- | --- |
| `validate_docs.py` | `PASS`, 51 Markdown | estructura/relaciones; no verdad o suficiencia. |
| `test_validate_docs.py` | `PASS`, 24 mutaciones negativas y una autorización positiva | añade encabezado/ID/campo duplicado `PROP`, existencia/navegación/correspondencia canónica de `DEC` y contrato de diff del workflow. |
| `test_select_proposals.py` | `PASS` | fecha, identidad de evento, evidencia, ejecución vacía, memoria acumulativa, repetición y cambio real. |
| `test_workflow_diff.py` | `PASS` | repositorio Git temporal: rechaza whitespace comprometido y acepta la corrección en rango base…candidata. |
| Ensayo CLI con checkpoint temporal | primera salida `PROP-001: evento,evidencia_nueva`; segunda `NO_SELECTION` | no es una automatización activada ni una política de notificación. |
| Workflow YAML y `git diff --check` | `PASS` local | sintaxis y rango comprobados localmente. |
| GitHub Actions `documentation / validate` | `PASS`, 6 s, [ejecución final 38729105629](https://github.com/ivanes189/hosteleria-app-product-docs/actions/runs/38729105629/job/116402177526) | head fusionado `5b7c5e90…`; no era check obligatorio según la consulta posterior. |

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

Se conservan el procedimiento único, `CHG`, `PROP` plano, validador y fixtures. Se omiten por ahora skill de Codex, dashboard, base de datos y programación periódica. Los controles mecánicos funcionan en local y en la ejecución de PR; la revisión independiente concluyó. Falta observar fricción y utilidad sostenida en cambios reales posteriores.

## Revisión, DOC-GATE y siguiente acto

La revisión propia durante la preparación es interna, no independiente. La única instancia GPT-6 Astra configurada según [SRC-018](../../investigacion/SOURCE_REGISTER.md#src-018) emitió [C0 `NO APTO`](../../gobierno/revisiones/DICTAMEN_CHG-002-C0.md) para `36d071fb…`. Tras preservar y abrir C1, la misma instancia emitió [C1 `NO APTO`](../../gobierno/revisiones/DICTAMEN_CHG-002-C1.md) para `e86f3674…`: RI-001, RI-003 y RI-004 resueltos; RI-002 parcialmente resuelto. Candidata y dictamen C1 se preservaron antes de abrir C2. La misma instancia emitió [C2 `APTO`](../../gobierno/revisiones/DICTAMEN_CHG-002-C2.md) para `4246943b…`: RI-002 resuelto, sin hallazgos nuevos ni regresiones directas. C1 y C2 quedan consumidos; no se abre C3. Coste/consumo expuesto: `desconocido`.

`DOC-GATE: PASSED` para la candidata exacta `4246943b9ef288e0a437819d89934e2c08e634f4`. La [PR #1](https://github.com/ivanes189/hosteleria-app-product-docs/pull/1) fue fusionada por Iván el 2026-10-15 como squash `a8365b6674381c4c23985bdce4a58a178c5c4a69`; su árbol coincide exactamente con el head `5b7c5e90901f753ffdebc47a9443ba0cfe1b49b8` y el check final pasó. `incorporation_status: integrada`. El cierre post-fusión es una conciliación factual proporcional tramitada mediante flujo ordinario separado: no cambia política, procedimiento, validador ni candidata revisada. Siguiente transición: D3, observar el circuito en cambios reales antes de simplificarlo, extenderlo o activar periodicidad.
