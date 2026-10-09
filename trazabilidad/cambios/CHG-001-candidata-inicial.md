---
id: CHG-001
title: Candidata documental inicial
doc_type: document_change
summary: Reconstrucción inicial, gobierno, ejemplo de mesa 12 y controles.
updated_at: 2026-10-09
source_refs: [SRC-001, SRC-002, SRC-003, SRC-004, SRC-005, SRC-006, SRC-007, SRC-008]
incorporation_status: candidata_externa
---

# CHG-001 — Candidata documental inicial

[← Cambios](README.md)

## Base, motivo y alcance

Base externa sin commit; destino remoto privado no verificable. Motivo: crear una fuente viva y navegable a partir del prompt maestro, conversación accesible, seis repositorios y fuentes oficiales. Incluye toda la candidata; excluye creación remota, commits, PR, CI, permisos, automatizaciones y desarrollo.

## Impacto

| Área/rutas | Resultado | Justificación/evidencia |
| --- | --- | --- |
| `README.md`, tres entradas y sus índices | actualización realizada | navegación, audiencia, contenido/exclusiones e índices explícitos. |
| `decisiones/`, `requisitos/`, `validacion/` | actualización realizada | autoridad, [REQ-012](../../requisitos/REQUIREMENTS.md#req-012), TEST-007/008/009 y relaciones navegables. |
| `producto/`, `operacion/`, `catalogo/` | actualización realizada | caso mesa 12, estados honestos y oferta no acreditada. |
| `arquitectura/`, `cumplimiento/` | actualización realizada | límites deterministas, eventos, integraciones, privacidad y enlaces de colección. |
| `investigacion/` | actualización realizada | commits, rutas/permalinks, naturaleza de evidencia y cobertura fijados. |
| `trazabilidad/`, `CHANGELOG.md` | actualización realizada | matriz enlazada, vacíos visibles, expediente e historia. |
| `DOCUMENTATION_POLICY.md`, `plantillas/` | actualización realizada | estados por tipo, invalidación, familias auxiliares, ciclo/revisor/coste y plantilla CHG. |
| `herramientas/` | actualización realizada | validación estructural ampliada y siete pruebas negativas. |
| `gobierno/` | actualización realizada | auditoría de autoridad, estado, revisión y manifiestos preservados. |
| Implementación del producto | revisado sin modificación | no hay evidencia accesible suficiente para afirmar estado positivo o negativo. |
| Repositorios fuente | revisado sin modificación | copias temporales, en solo lectura; no se ejecutó código o pruebas. |
| GitHub remoto/controles | bloqueado fuera del lote | autenticación inválida y plan/existencia privada desconocidos; no impide evaluar la candidata externa. |

## Ciclos y revisión

| Etapa | Candidata | Hallazgos | Resultado |
| --- | --- | --- | --- |
| Redacción inicial | manifiesto SHA-256 `09ff077de7c68e9876c9358e7aa5fb21cdafd51b53e6acfa3df3a5bc18eea307` (45 entradas) | RI-001–RI-007 | revisión completa `NO APTO`; `DOC-GATE: OPEN` |
| C1 de 2 — abierto 2026-10-09 | preimagen anterior; manifiesto preservado en `gobierno/revisiones/manifest-pre-c1.sha256` | RI-001–RI-007 | correcciones aplicadas; pendiente revalidación enfocada de la misma instancia |
| C2 de 2 — abierto 2026-10-09 | C1, manifiesto SHA-256 externo `9cd6da50a4a1f69b57bcc36737d11da00278bd92dcde0781fd244b767a9608e4`; preservado en `gobierno/revisiones/manifest-c1.sha256` | remanentes RI-001/002/003/004/006/007 | `abierto`; última corrección ordinaria limitada a los cierres descritos por la revisora |

La redacción no consume ciclo. C1 y C2 están consumidos desde su apertura aunque fallen o no produzcan cambios. No se autoriza C3.

## Validaciones

| Control | Resultado C1 | Evidencia |
| --- | --- | --- |
| Estructura, campos, estados, relaciones, IDs, enlaces, anclas, alcance e historia | `PASS` | `python3 herramientas/validate_docs.py`: 45 Markdown, sin errores. |
| Fixtures negativos | `PASS` | siete mutaciones detectadas por `python3 herramientas/test_validate_docs.py`. |
| Secretos evidentes | control de cierre C2 | resultado ligado al manifiesto congelado en el informe externo de ejecución. |
| Manifiesto | control de cierre C2 | `candidate-manifest.sha256`; huella externa posterior para evitar autorreferencia. |
| Revisión independiente | C1 `NO APTO`; C2 pendiente en esta imagen | veredicto final de la misma instancia ligado al manifiesto C2 en el informe externo. |

Aprobación humana e incorporación no forman parte de esta ejecución. Coste/consumo de revisión: `desconocido`, no expuesto por las herramientas disponibles.

## DOC-GATE

`OPEN` dentro de esta imagen hasta que el informe externo ligue los controles y el veredicto a su manifiesto exacto. Ese informe puede declarar `PASSED` sin modificar los bytes revisados; publicación e incorporación seguirán pendientes y fuera de este gate.
