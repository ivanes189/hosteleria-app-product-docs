---
id: CHG-003
title: Primera observación real del circuito documental
doc_type: document_change
summary: Conciliar la fusión de la PR 2 y registrar la primera observación de D3 sin extender el circuito.
updated_at: 2026-10-15
source_refs: [SRC-019, SRC-020, SRC-021]
incorporation_status: integrada
---

# CHG-003 — Primera observación real del circuito documental

[← Cambios](README.md)

## Base, motivo, clasificación y alcance

Base exacta: `main@1235b74b5ef17dcb14cce6c948246caa187d3be0`, squash de la [PR #2](https://github.com/ivanes189/hosteleria-app-product-docs/pull/2). Rama local: `codex/documentacion-viva-d3-observacion-1`. Clasificación: conciliación factual y observación del proceso; no cambia producto, política, procedimiento, validador ni workflow.

La PR #2 fue el primer cambio real posterior a la implantación de CHG-002 que recorrió rama, declaración de impacto, validación local, PR, CI y fusión humana. Este expediente registra el resultado como `OBS-001`; una sola observación no acredita utilidad sostenida ni permite extender el circuito.

## Impacto documental

| Área/rutas | Estado | Motivo/evidencia |
| --- | --- | --- |
| `gobierno/PROJECT_STATE.md`, `planificacion/ROADMAP.md`, `README.md` | actualización realizada | Sustituir la base anterior por `main@1235b74…` y marcar D3 en observación, no completada. |
| `investigacion/SOURCE_REGISTER.md` | actualización realizada | Añadir `SRC-020` con PR, head, check, squash y límites de la consulta. |
| `planificacion/PROPUESTAS_FUTURAS.md` | actualización realizada | Registrar una primera observación insuficiente para `PROP-001`; autorización y ejecución siguen pendientes. |
| `trazabilidad/TRACEABILITY_MATRIX.md`, `trazabilidad/cambios/README.md`, `CHANGELOG.md` | actualización realizada | Hacer navegable el expediente y conservar el hito. |
| `decisiones/DEC-004-documentacion-viva-minima.md`, `gobierno/PROCEDIMIENTO_DOCUMENTACION_VIVA.md`, `DOCUMENTATION_POLICY.md` | revisado sin modificación | La decisión y el flujo siguen siendo aplicables; una muestra no justifica una nueva regla. |
| Herramientas, fixtures y workflow documental | revisado sin modificación | Se ejecutan tal como están; no se observó un defecto que requiera cambiarlos. |
| Producto, arquitectura, operación, privacidad y permisos | no aplicable | La evidencia solo describe el proceso documental. |
| FDA, Agent OS y otros repositorios | no aplicable / no modificados | `PROP-001` permanece aplazada y sin autorización. |

## Dependencias, candidata y trabajo abierto

- Dependencias: [DEC-004](../../decisiones/DEC-004-documentacion-viva-minima.md), [CHG-002](CHG-002-documentacion-viva.md), [SRC-019](../../investigacion/SOURCE_REGISTER.md#src-019) y [SRC-020](../../investigacion/SOURCE_REGISTER.md#src-020).
- Candidata sustantiva exacta: `68c7b447d1fb53310986f49f6eb6c4a87d216790`, hija directa de `main@1235b74b5ef17dcb14cce6c948246caa187d3be0`.
- Trabajo abierto: acumular al menos dos cambios reales posteriores adicionales antes de reevaluar la condición cuantitativa de `PROP-001`; la utilidad y el coste de adopción requieren además juicio humano.

## Validaciones y evidencias posteriores

Comprobaciones ejecutadas antes y repetidas sobre la candidata exacta `68c7b447d1fb53310986f49f6eb6c4a87d216790` con árbol limpio:

| Control | Resultado | Límite |
| --- | --- | --- |
| `validate_docs.py` | `PASS`, 55 Markdown | Estructura y relaciones; no verdad semántica. |
| `test_validate_docs.py` | `PASS`, 24 mutaciones negativas y una autorización positiva | Demuestra rechazo/aceptación de los casos implementados. |
| `test_select_proposals.py` | `PASS` | Prueba el selector; no activa periodicidad. |
| `test_workflow_diff.py` | `PASS` | Ensayo Git local; no es una ejecución remota nueva. |
| Carga YAML del workflow | `PASS` | Sintaxis local; el workflow no se modifica. |
| `git diff --check` | `PASS` | Limpieza mecánica del parche. |

## Revisión y costes observables

La revisión del autor comprueba alcance, fuentes, coherencia e impacto. No se exige revisión independiente: el lote es factual y de observación, no cambia producto, arquitectura, privacidad, permisos, procedimiento crítico, gobierno, validador ni workflow. Tiempo humano no medido; coste/consumo no expuesto, `desconocido`.

## OBS-001 — PR #2 y cierre factual de CHG-002

| Aspecto | Evidencia observada | Resultado provisional |
| --- | --- | --- |
| Identidad | base `a8365b66…`, head `bdcc6c4a…`, squash `1235b74b…`; árboles de head y squash idénticos | La separación entre candidata e incorporación evitó transferir silenciosamente el dictamen previo. |
| Controles | validaciones locales en PASS y `documentation / validate` remoto en PASS (6 s) | El mismo conjunto mínimo fue reproducible en local y PR; no acredita verdad semántica ni obligatoriedad del check. |
| Impacto | diez documentos de estado/relación; ninguna herramienta o definición de producto | La declaración de impacto mantuvo acotado el lote. |
| Autoridad | publicación/PR autorizadas por Iván; fusión realizada por Iván | Se respetó la separación entre preparación, publicación y fusión humana. |
| Fricción | el SHA de squash solo existe tras la fusión y una frase transitoria sobre autorización quedó obsoleta antes de publicar | Conviene preferir hechos duraderos y registrar el resultado de una fusión en el siguiente cambio sustantivo, salvo contradicción que exija corrección inmediata. |
| Coste | CI: 6 s; tiempo humano y consumo de herramientas no expuestos | No existe base para afirmar ahorro o coste aceptable. |

Se conservan por ahora el `CHG`, la declaración de impacto, las identidades exactas, las pruebas locales, CI de PR y fusión humana. No se simplifica ni retira ninguna pieza con una sola muestra. `OBS-001` aporta una observación documental real, pero por su carácter de cierre ofrece evidencia débil para una transferencia entre proyectos.

## Manifiesto exacto, DOC-GATE y siguiente acto condicionado

`DOC-GATE: PASSED` para la candidata exacta `68c7b447d1fb53310986f49f6eb6c4a87d216790`. La revisión proporcional del autor y todas las comprobaciones exigibles pasaron; no se transfiere a este lote el dictamen independiente de CHG-002. La identificación y el cierre del gate se incorporan en un commit posterior de evidencia que no cambia `OBS-001` ni sus conclusiones.

Tras [autorización expresa](../../investigacion/SOURCE_REGISTER.md#src-021), la rama se publicó y se abrió la [PR #3](https://github.com/ivanes189/hosteleria-app-product-docs/pull/3). Iván la fusionó como squash `0478a8e7fc6ab799b4af1876a421bc532424133b`; su árbol coincide exactamente con el head `add0935044bfb99669919b6ebda53e742dcf1fb9` y el check final pasó en 7 s. `incorporation_status: integrada`.

La conciliación de esos hechos queda preparada localmente para agruparla con el siguiente cambio sustantivo, sin abrir una PR exclusiva de cierre. D3 permanece abierta: requiere cambios reales adicionales y juicio humano antes de simplificar, extender o transferir el circuito.
